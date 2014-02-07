Name:      qmailtoaster-util
Summary:   QMailToaster Utilities
Version:   2.0
Release:   0%{?dist}
License:   GPL
Group:     System Environment/Base
Vendor:    QmailToaster
Packager:  Eric Shubert <qmt-build@datamatters.us>
URL:       http://qmailtoaster.com/

Requires:  wget
Requires:  yum-priorities
Obsoletes: qmailtoaster-plus

Source1:   qt-install-repoforge
Source2:   qt-install-epel
Source3:   qt-mysql-secure-vpopmail
Source4:   qt-setup-firewall
Source5:   qt-install-dns-resolver
Source6:   qt-install

BuildArch: noarch
BuildRoot: %{_topdir}/BUILDROOT/%{name}-%{version}-%{release}.%{_arch}

%define BASE_DIR   /opt/%{name}
%define BIN_DIR    %{BASE_DIR}/bin
%define DOC_DIR    %{BASE_DIR}/doc
%define CONF_DIR   %{BASE_DIR}/etc
%define BIN_LINK   %{_bindir}
%define DOC_LINK   %{_docdir}

#-------------------------------------------------------------------------------
%description
#-------------------------------------------------------------------------------
This package contains utility scripts for QMailToaster.
It replaces what was formerly known as the qmailtoaster-plus package.

#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------
%setup -cT

#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------
%{__rm} -rf %{buildroot}

%{__mkdir_p} %{buildroot}%{BIN_DIR}
#%{__mkdir_p} %{buildroot}%{DOC_DIR}
#%{__mkdir_p} %{buildroot}%{CONF_DIR}
%{__mkdir_p} %{buildroot}%{BIN_LINK}
#%{__mkdir_p} %{buildroot}%{DOC_LINK}

%{__install} -p %{SOURCE1} %{buildroot}%{BIN_DIR}/qt-install-repoforge
%{__install} -p %{SOURCE2} %{buildroot}%{BIN_DIR}/qt-install-epel
%{__install} -p %{SOURCE3} %{buildroot}%{BIN_DIR}/qt-mysql-secure-vpopmail
%{__install} -p %{SOURCE4} %{buildroot}%{BIN_DIR}/qt-setup-firewall
%{__install} -p %{SOURCE5} %{buildroot}%{BIN_DIR}/qt-install-dns-resolver
%{__install} -p %{SOURCE6} %{buildroot}%{BIN_DIR}/qt-install

%{__ln_s} ../..%{BIN_DIR}/qt-install-repoforge      %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-install-epel           %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-mysql-secure-vpopmail  %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-setup-firewall         %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-install-dns-resolver   %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-install                %{buildroot}%{BIN_LINK}/.

#-------------------------------------------------------------------------------
%clean
#-------------------------------------------------------------------------------
%{__rm} -rf %{buildroot}

#-------------------------------------------------------------------------------
%files
#-------------------------------------------------------------------------------
%defattr(0644, root, root, 0755)

# directories
%dir %{BASE_DIR}
%dir %{BIN_DIR}
#%dir %{CONF_DIR}
#%dir %{DOC_DIR}

# files
%attr(0755, root, root)  %{BIN_DIR}/*
#%config(noreplace)       %{CONF_DIR}/*

# symlinks
%{BIN_LINK}/*

#-------------------------------------------------------------------------------
%post
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
%changelog
#-------------------------------------------------------------------------------
* Fri Feb  7 2014 Eric Shubert <eric@datamatters.us> - 1.0-0.qt
- Added qt-install-epel script
* Fri Dec 27 2013 Eric Shubert <eric@datamatters.us> - 1.0-0.qt
- Added qt-setup-firewall script
- Added qt-install-dns-resolver script
- Added qt-install script
* Sat Dec 21 2013 Eric Shubert <eric@datamatters.us> - 1.0-0.qt
- Added qt-mysql-secure-vpopmail script
* Mon Dec 16 2013 Eric Shubert <eric@datamatters.us> - 1.0-0.qt
- Initial package.
