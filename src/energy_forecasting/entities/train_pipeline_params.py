from typing import Dict, Any, Union

from dataclasses import dataclass
from .split_params import SplittingParams
from .feature_params import FeatureParams
from .path_params import PathParams
from marshmallow_dataclass import class_schema


@dataclass()
class TrainingPipelineParams:
    path_config: PathParams
    splitting_params: SplittingParams
    feature_params: FeatureParams
    train_params: Dict[str, Any]


TrainingPipelineParamsSchema = class_schema(TrainingPipelineParams)