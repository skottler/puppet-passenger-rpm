Sources and spec for building RPM's to run your puppet master under Passenger. This package simply installs the httpd configuration and rack configuration file and is not intended to be a soup-to-nuts solution for getting a master running. You'll already need certificates setup for installation to work properly.

## Building

1. `sudo mock -r epel-6-x86_64 --spec=puppet-passenger.spec --sources=. --resultdir=. --buildsrpm --verbose`
2. `sudo mock -r epel-6-x86_64 *.src.rpm --verbose`

## Copyright

Copyright (c) 2013 Red Hat Inc.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.
