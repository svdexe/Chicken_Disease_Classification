from cnnClassifier.entity.config_entity import TrainingConfig
import tensorflow as tf
from pathlib import Path



class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config
        self.model = None
    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            str(self.config.updated_base_model_path)
        )
        self.compile_model()
    
    def compile_model(self):
        self.model.compile(
            optimizer=tf.keras.optimizers.SGD(learning_rate=self.config.params_learning_rate),
            loss=tf.keras.losses.CategoricalCrossentropy(),
            metrics=["accuracy"]
        )
    
    def train_valid_generator(self):
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=str(self.config.training_data),
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=0.2,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator

        self.train_generator = train_datagenerator.flow_from_directory(
            directory=str(self.config.training_data),
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )


    def train(self, callback_list: list):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        if not self.model:
            raise ValueError("Model hasn't been loaded. Call get_base_model() first.")

        if not self.model.optimizer:
            self.compile_model()

        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list
        )

        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(str(path))