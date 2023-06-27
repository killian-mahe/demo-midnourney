import json
import logging
import pathlib
from typing import List, Dict

from config import load_config

config = load_config("gallery")
logger = logging.getLogger(__name__)


def save_experiment(prompt: str, image: bytes):
    """Save the experiment (prompt and image) in the gallery folders.

    Parameters
    ----------
    prompt : str
        The prompt used to generate the image.
    image : bytes
        The generated image.
    """
    gallery_path = pathlib.Path(config["gallery_dir"])

    if not gallery_path.exists():
        gallery_path.mkdir(parents=True)

    experiment_path = create_experiment_path(gallery_path)

    with open(experiment_path.joinpath("image.png"), "wb") as file:
        file.write(image)

    with open(experiment_path.joinpath("prompt.json"), "w") as file:
        json.dump({"prompt": prompt}, file)


def create_experiment_path(gallery_path: pathlib.Path) -> pathlib.Path:
    """Create a new experiment path, increasing the folder number.

    Parameters
    ----------
    gallery_path : pathlib.Path

    Returns
    -------
    The newly create experiment folder path.
    """
    folders_name = [path.name for path in gallery_path.glob("*/") if path.is_dir()]

    if len(folders_name) == 0:
        experiment_path = gallery_path.joinpath("0/")
    else:
        experiment_path = gallery_path.joinpath(str(int(max(folders_name)) + 1))

    experiment_path.mkdir()

    return experiment_path


def load_experiments() -> List[Dict[str, str]]:
    """Load saved experiments

    Returns
    -------
    A list of experiments containing the prompt and the generated image path.
    """
    gallery_path = pathlib.Path(config["gallery_dir"])

    experiments = []
    for path in gallery_path.glob("*/"):
        if not path.is_dir():
            continue

        with open(path.joinpath("prompt.json"), "r") as file:
            prompt = json.load(file)["prompt"]

        experiments.append(
            {"prompt": prompt, "image_path": str(path.joinpath("image.png").absolute())}
        )

    return experiments
