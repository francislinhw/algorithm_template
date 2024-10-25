# AWS EC2 Tutorial

## Copy the pem file to the .ssh directory
cp ~/Downloads/EC2\ Tutorial.pem ~/.ssh/

## Authorize the pem file
chmod 400 ~/.ssh/EC2\ Tutorial.pem

## Connect to the EC2 instance

```bash
ssh -i "EC2 Tutorial.pem" ec2-user@18.212.114.158 # The Public DNS (IPv4) of the EC2 instance
```

## Basic AWS Shell Commands

```bash
# List all the files in the current directory
ls

# List all the files in the current directory with more details
ls -l

# Change the directory
cd /var/www/html

# Print the current directory
pwd

# Create a new directory
mkdir test

# Remove a directory
rmdir test

# Remove a directory and all its contents
rm -rf test

# Create a new file
touch test.txt

# Remove a file
rm test.txt

# Copy a file

cp test.txt test2.txt

# Move a file

mv test2.txt test3.txt

# Rename a file

mv test3.txt test4.txt

# Print the content of a file

cat test4.txt

# Print the content of a file with line numbers

cat -n test4.txt

# Print the content of a file with line numbers and line breaks

cat -b test4.txt

# Print the content of a file with line numbers and empty lines

cat -n -b test4.txt

# exit the shell
exit

# echo the content of a file
echo "Hello World" > test5.txt

# install docker
sudo yum install docker -y

# start docker
sudo service docker start

# docker compose
sudo yum install docker-compose -y

# install git
sudo yum install git -y

```
