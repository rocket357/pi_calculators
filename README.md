# pi_calculators
Designed to waste CPU cycles calculating pi

    $ uname -a
    OpenBSD test.my.domain 6.4 GENERIC.MP#6 amd64
    $ dmesg | grep "Intel(R)"
    cpu0: Intel(R) Core(TM)2 CPU 6400 @ 2.13GHz, 2128.25 MHz, 06-0f-06
    cpu1: Intel(R) Core(TM)2 CPU 6400 @ 2.13GHz, 2128.01 MHz, 06-0f-06
    $ # "spacing" set to -300...
    $ time ./uniform_distribution.py
    Current settings will give 44942328 divisions from 0.0 to 1.0 for a sample size of 2019812846059584
    samples: 2019812846059584 misses: 433455533238130
    math.pi       = 3.14159265359
    calculated pi = 3.14159267957
    Accuracy      = 99.999999
        6m27.87s real     4m44.61s user     1m42.26s system
