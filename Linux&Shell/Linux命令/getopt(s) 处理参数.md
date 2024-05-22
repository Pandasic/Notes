# getopt/getopts

> 参考；
>
> [https://cloud.tencent.com/developer/article/1671654#](https://cloud.tencent.com/developer/article/1671654#)

getopts，这是shell内置的一种处理参数的方法，可以处理单个字符选项，例如 -h 192.168.1.1 这种形式的参数

getopt，这是unix自带的一种处理命令行参数的方法，既可以处理单个字符选项，也可以处理长选项，例如：–host 192.168.1.1 或 –host=192.168.1.1

```shell
OPTIONS
       -a, --alternative
              Allow long options to start with a single '-'.

       -h, --help
              Output a small usage guide and exit successfully.  No other output is generated.

       -l, --longoptions longopts
              The long (multi-character) options to be recognized.  More than one option name may be specified at once, by separating the names with commas.  This option may be given more than once, the longopts are  cumulative.
              Each long option name in longopts may be followed by one colon to indicate it has a required argument, and by two colons to indicate it has an optional argument.

       -n, --name progname
              The name that will be used by the getopt(3) routines when it reports errors.  Note that errors of getopt(1) are still reported as coming from getopt.

       -o, --options shortopts
              The  short  (one-character)  options to be recognized.  If this option is not found, the first parameter of getopt that does not start with a '-' (and is not an option argument) is used as the short options string.
              Each short option character in shortopts may be followed by one colon to indicate it has a required argument, and by two colons to indicate it has an optional argument.  The first character of shortopts may be  '+'
              or '-' to influence the way options are parsed and output is generated (see section SCANNING MODES for details).

       -q, --quiet
              Disable error reporting by getopt(3).

       -Q, --quiet-output
              Do not generate normal output.  Errors are still reported by getopt(3), unless you also use -q.

       -s, --shell shell
              Set quoting conventions to those of shell.  If no -s argument is found, the BASH conventions are used.  Valid arguments are currently 'sh' 'bash', 'csh', and 'tcsh'.

       -u, --unquoted
              Do not quote the output.  Note that whitespace and special (shell-dependent) characters can cause havoc in this mode (like they do with other getopt(1) implementations).

       -T, --test
              Test  if  your  getopt(1)  is  this  enhanced  version or an old version.  This generates no output, and sets the error status to 4.  Other implementations of getopt(1), and this version if the environment variable
              GETOPT_COMPATIBLE is set, will return '--' and error status 0.

       -V, --version
              Output version information and exit successfully.  No other output is generated.

```

```sh
#处理参数，规范化参数
ARGS=`getopt -a -o n:c:H:N:G:D: --long name:,mem:,cpu:,host:,netmask:,gateway:,dns:,help -- "$@"`
if [ $? != 0 ];then
        echo "Terminating..."
        exit 1
fi
#重新排列参数顺序
eval set -- "${ARGS}"
#通过shift和while循环处理参数
while :
do
    case $1 in
        -n|--name)
            name=$2
            shift
            ;;
        -m|--mem)
            mem=$2
            shift
            ;;
        -c|--cpu)
            cpu=$2
            shift
            ;;
        -h|--host)
            host=$2
            shift
            ;;
        -n|--netmask)
            netmask=$2
            shift
            ;;
        -g|--gateway)
            gateway=$2
            shift
            ;;
        -d|--dns)
            dns=$2
            shift
            ;;
        --help)
            usage
            ;;
        --)
            shift
            break
            ;;
        *)
            echo "Internal error!"
            exit 1
            ;;
    esac
shift
done
echo "name: $name"
echo "mem: $mem"
echo "cpu: $cpu"
echo "host: $host"
echo "netmask: $netmask"
echo "gateway: $gateway"
echo "dns: $dns"
```

