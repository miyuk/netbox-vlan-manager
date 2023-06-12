ARG python_ver=3.8
FROM python:${python_ver}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME=/opt/netbox/netbox

# Install NetBox
ARG netbox_ver=master
RUN mkdir -p /opt
RUN git clone --single-branch --branch ${netbox_ver} https://github.com/netbox-community/netbox.git /opt/netbox/
RUN pip install --upgrade pip && \
    pip install -r /opt/netbox/requirements.txt

# Install Netbox Plugin
RUN mkdir -p /opt/plugin
COPY . /opt/plugin
RUN mkdir -p /opt/plugin && \
    cd /opt/plugin && \
    python /opt/plugin/setup.py develop

# Set Work Directory
WORKDIR $APP_HOME
