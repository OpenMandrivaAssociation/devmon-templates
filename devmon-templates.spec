Summary:	Templates for Devmon SNMP Device Monitoring for Hobbit/BigBrother
Name:		devmon-templates
Version:	20080206
Release:	7
License:	GPLv2+
Group:		Monitoring
Url:		http://devmon.sf.net
Source0:	http://prdownloads.sourceforge.net/devmon/devmon-templates-%{version}.tar.gz
Source10:	%{name}.rpmlintrc
Requires:	devmon
BuildArch:	noarch

%description
Devmon is a device monitoring script which works in tandem with the
Hobbit/BigBrother monitoring suites. It queries remote hosts via SNMP, applies
user-defined logic and thresholds to the acquired data, and submits status and
alarms to a display server.

This package contains the device templates, which define the OIDs, transforms,
thresholds, exceptions, and the message template sent to Hobbit/Big Brother.

%files
%{_datadir}/devmon/templates

#----------------------------------------------------------------------------

%prep
%setup -q

%build

%install
install -d %{buildroot}/%{_datadir}/devmon/templates
cp -a * %{buildroot}/%{_datadir}/devmon/templates

