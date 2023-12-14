"""Flow config module."""

from dataclasses import dataclass, field
from typing import Dict

from uniflow.extract.config import Config as ExtractConfig
from uniflow.model.config import (
    HuggingfaceModelConfig,
    LMQGModelConfig,
    ModelConfig,
    OpenAIModelConfig,
)
from uniflow.schema import GuidedPrompt


@dataclass
class Config:
    """Flow Config Class."""

    flow_name: str = "BaseModelFlow"
    guided_prompt_template: GuidedPrompt = GuidedPrompt()
    num_thread: int = 1
    model_config: ModelConfig = ModelConfig()


@dataclass
class OpenAIConfig:
    """OpenAI Flow Config Class."""

    flow_name: str = "OpenAIModelFlow"
    guided_prompt_template: GuidedPrompt = GuidedPrompt()
    num_thread: int = 1
    model_config: ModelConfig = OpenAIModelConfig()


@dataclass
class HuggingfaceConfig:
    """Huggingface Config Class."""

    flow_name: str = "HuggingFaceModelFlow"
    guided_prompt_template: GuidedPrompt = GuidedPrompt()
    num_thread: int = 1
    model_config: ModelConfig = HuggingfaceModelConfig()


@dataclass
class LMQGConfig:
    """LMQG Config Class."""

    flow_name: str = "LMQGModelFlow"
    num_thread: int = 1
    guided_prompt_template: Dict[str, str] = field(default_factory=lambda: {})
    model_config: ModelConfig = LMQGModelConfig()


@dataclass
class PipelineConfig:
    """Pipeline Config Class."""

    extract_config: ExtractConfig = ExtractConfig()
    transform_config: Config = OpenAIConfig()
