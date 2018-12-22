FROM pytorch/pytorch:latest

RUN git clone -b develop https://github.com/kakao/khaiii.git
WORKDIR /workspace/khaiii

RUN pip install cython
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN pip install cmake
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
RUN pip install .

WORKDIR /workspace/khaiii/build
