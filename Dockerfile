FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY agent_webrtc_stream/ ./agent_webrtc_stream/
COPY tests/ ./tests/

RUN pip install --no-cache-dir -e .

ENTRYPOINT ["agent-webrtc-stream"]
CMD ["stream"]
