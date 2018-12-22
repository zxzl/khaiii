FROM ubuntu:16.04

RUN apt-get update
RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update

# Install Python 3.6
RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN apt-get install -y git

# Link `python3` to Python 3.6 instead of Python 3.6
RUN rm -rf /usr/bin/python3
RUN ln -s /usr/bin/python3.6 /usr/bin/python3
RUN python3 --version

RUN python3 -m pip install pip --upgrade
RUN python3 -m pip install wheel

RUN git clone -b develop https://github.com/kakao/khaiii.git /workspace/khaiii
WORKDIR /workspace/khaiii

RUN pip3 install cython
RUN pip3 install -r requirements.txt

RUN pip3 install cmake
RUN mkdir build

WORKDIR /workspace/khaiii/build

RUN cmake ..
RUN make all
RUN make resource

RUN apt-get update -y
RUN apt-get install -y language-pack-ko
RUN locale-gen en_US.UTF-8
RUN update-locale LANG=en_US.UTF-8

RUN make install
RUN make package_python
WORKDIR /workspace/khaiii/build/package_python
RUN pip3 install .
ENV PYTHONIOENCODING=utf8

RUN pip3 install jupyter
EXPOSE 8888
WORKDIR /workspace/khaiii/build
ENTRYPOINT ["jupyter", "notebook", "--ip=0.0.0.0", "--allow-root"]

