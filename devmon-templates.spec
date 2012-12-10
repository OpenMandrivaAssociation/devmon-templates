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


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 20080206-5mdv2011.0
+ Revision: 617575
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 20080206-4mdv2010.0
+ Revision: 427961
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 20080206-3mdv2009.0
+ Revision: 244080
- rebuild

* Wed Feb 06 2008 Buchan Milne <bgmilne@mandriva.org> 20080206-1mdv2008.1
+ Revision: 163086
- import devmon-templates


