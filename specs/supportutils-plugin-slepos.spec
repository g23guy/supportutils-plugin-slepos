#
# spec file for package supportutils-plugin-slepos (Version 1.0-3)
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
Release:      4
Source:       %{name}-%{version}.tar.gz
Summary:      Supportconfig Plugin for SLEPOS
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Distribution: Novell NTS
Vendor:       Novell Technical Services
Requires:     supportconfig-plugin-resource
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

%prep
%setup -q
%build
gzip -9f slepos-plugin.8

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/opt/supportconfig/plugins
install -d $RPM_BUILD_ROOT/usr/share/man/man8
install -m 0544 slepos $RPM_BUILD_ROOT/opt/supportconfig/plugins
install -m 0644 slepos-plugin.8.gz $RPM_BUILD_ROOT/usr/share/man/man8/slepos-plugin.8.gz

%files
%defattr(-,root,root)
/opt/supportconfig/plugins/*
/usr/share/man/man8/slepos-plugin.8.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog -n supportutils-plugin-slepos

