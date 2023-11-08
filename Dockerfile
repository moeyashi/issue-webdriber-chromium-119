FROM python:3.9

ENV PYTHONUNBUFFERED=1 \
  \
  PYTHONPATH="/workspace/src:$PYTHONPATH" \
  \
  LANGUAGE=ja_JP.UTF-8 \
  LANG=ja_JP.UTF-8

WORKDIR /workspace

RUN apt-get update \
  && apt-get install --no-install-recommends -y \
  # chromium \
  locales \
  && locale-gen ja_JP.UTF-8 \
  && apt-get install -y --no-install-recommends fonts-ipafont
