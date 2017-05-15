FROM debian


RUN apt-get update
RUN apt-get install -y arp-scan

CMD arp-scan --interface=eth0 --localnet
