# RanPassCLI
Simple Random Password Generator CLI Tool.

## Installing
To install this CLI tool you can run the below command
```
pip install ranpasscli
```

The above commands would install the package globally and `ranpasscli` will be available on your system.

## How to use
Generate a random password
```
ranpasscli <length of password desired> -f <number of password format option>
```
There are four options for password formats:

1. Alphabetic lowercase
2. Alphabetic mixed case
3. Alphanumeric mixed case (Default option)
4. Alphanumeric mixed case + special characters

If you want to see these options in the terminal, run `ranpasscli -h` or `ranpasscli --help` to open the help page.

If no `<length>` is given the default is 10.