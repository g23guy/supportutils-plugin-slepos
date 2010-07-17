#
# spec file for package supportutils-plugin-slepos (Version 0.0.0)
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
Version:      0.0
Release:      2
Source:       %{name}-%{version}.tar.gz
Summary:      Supportconfig Plugin for SLEPOS
BuildRoot:    %{_tmppath}/%{name}-%{version}-build
BuildArch:    noarch
Distribution: Novell NTS
Vendor:       Novell Technical Services
Requires:     supportconfig-plugin-resource-0.0.1
Requires:     slepos-release

%description
Supportconfig plugin for SUSE Linux Enterprise Point of Sale (SLEPOS). 
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
gzip -9f slepos-plugin.5

%install
pwd;ls -la
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/opt/supportconfig/plugins
install -d $RPM_BUILD_ROOT/usr/share/man/man5
install -m 0400 slepos $RPM_BUILD_ROOT/opt/supportconfig/plugins
install -m 0644 slepos-plugin.5.gz $RPM_BUILD_ROOT/usr/share/man/man5/slepos-plugin.5.gz

%files
%defattr(-,root,root)
/opt/supportconfig/plugins/*
/usr/share/man/man5/slepos-plugin.5.gz

%clean
rm -rf $RPM_BUILD_ROOT

%changelog -n supportutils-plugin-slepos

