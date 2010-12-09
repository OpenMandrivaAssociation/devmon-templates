%{!?mdkversion:%define notmdk}

Name:		devmon-templates
Version:	20080206
Release:	%mkrel 5
Summary:	Templates for Devmon SNMP Device Monitoring for Hobbit/BigBrother
License:	GPL
Group:		Monitoring
URL:		http://devmon.sf.net
Source:		http://prdownloads.sourceforge.net/devmon/devmon-templates-%{version}.tar.gz
BuildArch:	noarch
%if %{!?notmdk:1}%{?notmdk:0}
Requires(pre):	rpm-helper
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Requires:	devmon-templates >= 20080206

%description
Devmon is a device monitoring script which works in tandem with the
Hobbit/BigBrother monitoring suites. It queries remote hosts via SNMP, applies
user-defined logic and thresholds to the acquired data, and submits status and
alarms to a display server.

This package contains the device templates, which define the OIDs, transforms,
thresholds, exceptions, and the message template sent to Hobbit/Big Brother.

%prep
%setup -q

%build

%install
rm -Rf %{buildroot}
install -d %{buildroot}/%{_datadir}/devmon/templates
cp -a * %{buildroot}/%{_datadir}/devmon/templates

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/devmon/templates
