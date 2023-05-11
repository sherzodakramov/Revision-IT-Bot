# CRM Telegram Bot of Revision IT Group
--------------

1. Configuring Database
------------
# OS: Ubuntu
<details>

<summary>Installing Postgresql</summary>

### Updating system and installing postgresql

First of all update system

```bash
sudo apt update
```

Upgrade if it needed

```bash
sudo apt upgrade
```

Install postgresql

```bash
sudo apt install postgresql postgresql-contrib
```

Staring postgresql service

```bash
sudo systemctl start postgresql.service
```

Enabling to autostart with OS

```bash
sudo systemctl enable postgresql.service
```

Running psql command with postgres user

```bash
sudo -i -u postgres
psql
```
You can exit with command:
```bash
\q
exit
``` 

Or with this way:
```bash
sudo -u postgres psql
\q
```

### Creating new user and set password

Creating new user to our tg bot
```bash
sudo -u postgres createuser --interactive
Enter name of role to add: revisiontgbot
Shall the new role be a superuser? (y/n) y
sudo -u postgres createdb revisiontgbot
sudo adduser revisiontgbot
```

Checking if it's okay
```bash
sudo -u revisiontgbot psql
\conninfo
```
Result should be
```bash
You are connected to database "revisiontgbot" as user "revisiontgbot" via socket in "/var/run/postgresql" at port "5432".
```

Changing password for revisiontgbot user
```bash
sudo -u postgres psql template1
ALTER USER revisiontgbot PASSWORD 'akramoff1722';
```

</details>

------------
2. Configuring Python

<details>

<summary>Installing pyTelegramBotAPI library for Python</summary>

# OS: Ubuntu

```bash
pip3 install pyTelegramBotAPI
```

# OS: Windows

```bash
pip install pyTelegramBotAPI
```

</details>

<details>

<summary>Installing Psycopg database adapter to the Python for using PostgreSQL</summary>

# OS: Ubuntu

```bash
pip3 install psycopg2
```

# OS: Windows

```bash
pip install psycopg2
```

</details>

<details>

<summary>Installing Python Decouple for using virtual environment variables</summary>

# OS: Ubuntu

```bash
pip3 install python-decouple
```

# OS: Windows

```bash
pip install python-decouple
```

</details>

------------
3. Make migrations up

<details>

<summary>Migrate</summary>

# OS: Ubuntu

```bash
python3 migrations.py
```

# OS: Windows

```bash
python migrations.py
```

</details>

------------
4. Running

<details>

<summary>Running python</summary>

# OS: Ubuntu

```bash
python3 main.py
```

# OS: Windows

```bash
python migrations.py
```

</details>


Todo
----
 * Inline commands
 * Web App
 * Dashboard