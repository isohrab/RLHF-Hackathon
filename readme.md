# RLHF Hackathon

Welcome to the RLHF Hackathon repository! In this repo, we present several Jupyter notebooks to provide hands-on RLHF training. By the end of this hackathon, you will become familiar with basic RLHF techniques and be able to train a large language model (LLM) using Direct Policy Optimization (DPO) and Proximal Policy Optimization (PPO). Given that resources for a real LLM may not be available to everyone, we use the Phi-3 model and the unsloth library, allowing fine-tuning on a single GPU. The notebooks have been tested on an ml.g5.2xlarge instance.

:warning: **Please note that Phi-3 is already fine-tuned over a vast number of datasets. Our work in these notebooks is solely for demonstration purposes.**

## Notebooks

### Supervised Fine-Tuning
Notebook `01_SFT_with_unsloth` provides simple steps for performing supervised fine-tuning (SFT) using a dataset and preparing the records based on the LLM chat format.

### Generate RLHF Dataset
Notebook `02_RLHF_dataset` demonstrates how to gather feedback from humans. This notebook uses the previously fine-tuned LLM to generate different responses for the same prompt and then selects the best response based on human feedback.

### DPO
Notebook `03_DPO_with_unsloth` demonstrates how to use the DPO technique with the TRL library. It shows how to prepare the dataset for the LLM chat format and the DPOTrainer function.

## PPO
The notebook `04_PPO` demonstrates how to use the PPO technique with the TRL library. In this notebook, we will show you how to perform RLHF using a reward model with GPT-2 as the base model.

## Acknowledgement
This Hackathon is part of the MHP internal Hackathon event series.

## Resources
1. [DPO - Align LLMs in 2024 with TRL by Phil Schmid](https://www.philschmid.de/dpo-align-llms-in-2024-with-trl)
2. [unsloth GitHub repository](https://github.com/unslothai/unsloth)
3. [Hugging Face TRL documentation](https://huggingface.co/docs/trl/en/index)
4. [PPO notebook](https://gist.github.com/bigsnarfdude/b4319115a8bd302d053d52729f262c62)

## Contributors
Alireza, Milos, Josefine