Name:       puppet-passenger
Version:    1.0.0
Release:    1%{?dist}
Summary:    Run your puppet master under Passenger
Group:      System Environment/Base
License:    GPLv3
URL:        https://github.com/skottler/puppet-passenger-rpm

Requires:   httpd
Requires:   mod_passenger
Requires:   mod_ssl
Requires:   puppet

Source0:    puppetmaster.conf
Source1:    puppetmaster-config.ru

%description
Run your puppet master under Passenger.

%install
mkdir -p %{buildroot}%{_sysconfdir}/httpd/conf.d
mkdir -p %{buildroot}%{_sysconfdir}/puppet/rack
install -p %{SOURCE0} %{buildroot}%{_sysconfdir}/httpd/conf.d/puppetmaster.conf
install -p %{SOURCE1} %{buildroot}%{_sysconfdir}/puppet/rack/config.ru

%files
%attr(0644, puppet, puppet) %{_sysconfdir}/puppet/rack/config.ru
%{_sysconfdir}/httpd/conf.d/puppetmaster.conf

%post
sed -i "s/squigley.namespace.at.pem/`hostname --fqdn`/" /etc/httpd/conf.d/puppetmaster.conf

%changelog
* Thu Sep 5 2013 Sam Kottler <shk@redhat.com> - 1.0.0-1
- Initial creation of the puppet-passenger package
