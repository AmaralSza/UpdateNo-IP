#######################################################
# Nome do Arquivo: UpdateNO_IP.sh
# Autor: William Amaral de Souza
# Data de Criação: 21/06/2023
# Versao: x.x.x
# Data Modificacao: dd/mm/aa
# Descrição: 
#######################################################
#!/bin/bash

# No lugar de @ usar %40
USUARIO="EmailDoLogin%40gmail.com"
PASSWORD="SenhaDoLogin"

# Nome do Host ativo
HOST="exemplodehost.zapto.org"

# Sem necessidade de alteracao
LOG="/tmp/noip.log"
LOG_IP="/tmp/ip_atual"
IP_OLD=$(cat $LOG_IP)
USERAGENT="Simple Bash No-IP Updater/0.4"
BUSCA_IP=$(wget -qO- http://ipecho.net/plain)

if [ ! -e $LOG_IP ]; then 
	touch $LOG_IP
fi

if [ "$BUSCA_IP" != "$IP_OLD" ]; then
	echo "Executando o update do IP" `date +%d/%m/%Y-%H:%M` >> $LOG
	curl  -s --user-agent "$USERAGENT" "https://$USUARIO:$PASSWORD@dynupdate.no-ip.com/nic/update?hostname=$HOST&myip=$BUSCA_IP" >> $LOG
	echo $BUSCA_IP > $LOG_IP
else
	echo "Sem necessidade de atualizacao:" `date +%d/%m/%Y-%H:%M` >> $LOG
fi

exit 0