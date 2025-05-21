
FROM vllm/vllm-openai:latest

ENV MODEL_NAME openai-community/gpt2

ENTRYPOINT python3 -m vllm.entrypoints.openai.api_server --model $MODEL_NAME $VLLM_ARGS