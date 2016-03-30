# Проект Cemona

Это подробная документация по проекту. Если какая-то информация устарела или не написана - просьба сообщить об этом, а еще лучше - исправить самому.

## Используемый стек технологий

* Фрэймворк [Django1.8.9](https://www.djangoproject.com/).
* СУБД [PostgreSQL9.4](http://www.postgresql.org/).
* [Python3.4](https://www.python.org/) - язык общего назначения.
* [Nginx](http://nginx.org/ru/) - сервер для отдачи статики.
* [WSGI HTTP Server](http://gunicorn.org/) - для проекта на релизе.

## SSH доступ на debian-сервер из под ubuntu

Если из коробки не работает, коннект виснет и закрывается спустя 1-2 минуты. Выполняем комунду соединения с параметрами дебага:
```
#!bash
$ ssh -v cemona@10.1.3.33
$ ...
$ debug1: sending SSH2_MSG_KEX_ECDH_INIT
$ debug1: expecting SSH2_MSG_KEX_ECDH_REPLY
$ Connection closed by 10.1.3.33
```
Если у вас похожая ситуация, делаем все по следующей иснтукции/
На локальной машине нужно настроить ssh-клиент, [подробнее](http://superuser.com/questions/699530/git-pull-does-nothing-git-push-just-hangs-debug1-expecting-ssh2-msg-kex-ecd).
Отредактировать файл ```/etc/ssh/ssh_config``` как показано на стеке.
Мой файл выглядит так:

    Host *
    #   ForwardAgent no
    #   ForwardX11 no
    #   ForwardX11Trusted yes
    #   RhostsRSAAuthentication no
    #   RSAAuthentication yes
    #   PasswordAuthentication yes
    #   HostbasedAuthentication no
    #   GSSAPIAuthentication no
    #   GSSAPIDelegateCredentials no
    #   GSSAPIKeyExchange no
    #   GSSAPITrustDNS no
    #   BatchMode no
    #   CheckHostIP yes
    #   AddressFamily any
    #   ConnectTimeout 0
    #   StrictHostKeyChecking ask
    #   IdentityFile ~/.ssh/identity
    #   IdentityFile ~/.ssh/id_rsa
    #   IdentityFile ~/.ssh/id_dsa
    #   Port 22
    #   Protocol 2,1
    #   Cipher 3des
    Ciphers aes128-ctr,aes192-ctr,aes256-ctr,arcfour256,arcfour128,aes128-cbc,3des-cbc
    MACs hmac-md5,hmac-sha1,umac-64@openssh.com,hmac-ripemd160
    #   EscapeChar ~
    #   Tunnel no
    #   TunnelDevice any:any
    #   PermitLocalCommand no
    #   VisualHostKey no
    #   ProxyCommand ssh -q -W %h:%p gateway.example.com
    #   RekeyLimit 1G 1h
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    GSSAPIDelegateCredentials no
    HostKeyAlgorithms ssh-rsa,ssh-dss

Сохраняем изменения в файле и соединяемся по ssh.