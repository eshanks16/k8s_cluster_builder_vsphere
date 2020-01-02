import re
import socket


class FilterModule(object):

    def filters(self):
        return {
            'kube_platform_version': self.kube_platform_version,
            'kube_debian_distro_version': self.kube_debian_distro_version,
            'kube_lookup_hostname': self.kube_lookup_hostname,
        }

    def kube_lookup_hostname(self, ip, hostname, many=False):
        ips = set()

        ip = ip.split(':')[0]
        if ip and ip != "":
            if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip):
                ips.add(ip)
        try:
            (_, _, iplist) = socket.gethostbyname_ex(hostname)
            ips |= set(iplist)
        except socket.error as e:
            pass

        if many:
            ips.add(hostname)
            return sorted(list(ips))
        else:
            return sorted(list(ips))[0]

    def kube_platform_version(self, version, platform):
        match = re.match('(\d+\.\d+.\d+)\-(\d+)', version)
        if not match:
            raise Exception("Version '%s' does not appear to be a "
                            "kubernetes version." % version)
        sub = match.groups(1)[1]
        if len(sub) == 1:
            if platform.lower() == "debian":
                return "%s-%s" % (match.groups(1)[0], '{:02d}'.format(sub))
            else:
                return version
        if len(sub) == 2:
            if platform.lower() == "redhat":
                return "%s-%s" % (match.groups(1)[0], int(sub))
            else:
                return version

        raise Exception("Could not parse kubernetes version")

    def kube_debian_distro_version(self, distro):
        if distro.lower() in ("xenial", "bionic",):
            return "kubernetes-xenial"
        return "kubernetes-%s" % distro.lower()