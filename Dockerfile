FROM python:3.12.4-slim-bookworm

ARG DEBIAN_FRONTEND="noninteractive"
ARG GROUP
ARG BROKER
ARG TOPIC

WORKDIR /rorschach_mask

COPY rorschach_mask /rorschach_mask/rorschach_mask
COPY requirements.txt /rorschach_mask
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "rorschach_mask"]