FROM ubuntu:latest
LABEL authors="arche"

ENTRYPOINT ["top", "-b"]