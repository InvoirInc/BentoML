import bentoml
from bentoml.adapters import DataframeInput
from bentoml.frameworks.sklearn import SklearnModelArtifact


@bentoml.env(infer_pip_packages=True)
@bentoml.artifacts([SklearnModelArtifact('model')])
class IrisClassifier(bentoml.BentoService):
    @bentoml.api(input=DataframeInput())
    def predict(self, df):
        return self.artifacts.model.predict(df)
