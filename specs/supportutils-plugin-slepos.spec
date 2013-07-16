#
# spec file for package supportutils-plugin-slepos (Version 1.0-4)
#
# Copyright (C) 2010 Novell, Inc.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#

# norootforbuild
# neededforbuild  

Name:         supportutils-plugin-slepos
URL:          https://code.google.com/p/supportutils-plugin-slepos/
License:      GPLv2
Group:        Documentation/SuSE
Autoreqprov:  on
Version:      1.0
Release:      8.1
Source:       %{name}-%{version}.tar.gz
Summary:      Supportconfig Plugin for SLEPOS
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Distribution: Novell NTS
Vendor:       Novell Technical Services
Requires:     supportconfig-plugin-resource
Requires:     supportconfig-plugin-tag
Requires:     slepos-release

%description
Supportconfig plugin for SUSE Linux Enterprise Point of Service (SLEPOS). 
Plugins extend supportconfig functionality and include the output in 
the supportconfig tar ball.

Please submit bug fixes or comments via:
    https://code.google.com/p/supportutils-plugin-slepos/issues/list

Authors:
--------
    Jason Record <jrecord@novell.com>
    Thomas Schlosser <schloss@suse.com>	

%prep
%setup -q
%build
gzip -9f slepos-plugin.8

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/lib/supportconfig/plugins
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -m 0544 slepos $RPM_BUILD_ROOT/usr/lib/supportconfig/plugins
install -m 0644 slepos-plugin.8.gz $RPM_BUILD_ROOT/usr/share/man/man8/slepos-plugin.8.gz

%files
%defattr(-,root,root)
/usr/lib/supportconfig
/usr/lib/supportconfig/plugins
/usr/lib/supportconfig/plugins/slepos
/usr/share/man/man8/slepos-plugin.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu Jul 04 2013 schloss@suse.com
-slepos 1.0.8
-modified for SLEPOS11 SP2
* Mon Oct 25 2010 jrecord@novell.com
-added requires supportconfig-plugin-tag
-changed /opt/supportconfig to /usr/lib/supportconfig
* Wed Sep 29 2010 jrecord@novell.com
-only requires supportconfig-plugin-resource
* Thu Jul 29 2010 schloss@suse.de 
-fixed SLEPOS element collisions
-slepos: 1.0.3
* Mon Jul 19 2010 jrecord@novell.com 
-updated required supportconfig-plugin-resource version
-slepos: 1.0.0
* Sat Jul 17 2010 jrecord@novell.com 
-initial build
