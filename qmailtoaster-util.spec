Name:      qmailtoaster-util
Summary:   QMailToaster Utilities
Version:   2.0
Release:   1%{?dist}
License:   GPL
Group:     System Environment/Base
Vendor:    QmailToaster
Packager:  Eric Shubert <qmt-build@datamatters.us>
URL:       http://qmailtoaster.com/

Requires:  wget
Requires:  yum-priorities
Obsoletes: qmailtoaster-plus

Source1:   mansfor
Source2:   qmail-clam
Source3:   qmail-spam
Source4:   qmHandle
Source5:   qmlog
Source6:   qmqtool
Source7:   qt-backup
Source8:   qt-bootstrap-1
Source9:   qt-bootstrap-2
Source10:  qt-config
Source11:  qt-install
Source12:  qt-install-dns-resolver
Source13:  qt-install-epel
Source14:  qt-install-repoforge
Source15:  qt-mysql-secure-vpopmail
Source16:  qt-prune-graylist
Source17:  qt-restore
Source18:  qt-setup-firewall
Source19:  queue_repair.py
Source20:  sa-stats
Source21:  qmlog-trim.sed
Source22:  artistic.txt
Source23:  gpl.txt
Source24:  licenses.txt
Source25:  qmHandle.doc.txt
Source26:  qmqtool.doc.txt
Source27:  qmqtool.faq.txt
Source28:  queue_repair.doc.txt

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
It replaces/obsoletes the former qmailtoaster-plus package.

#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------
%setup -cT

#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------
%{__rm} -rf %{buildroot}

%{__mkdir_p} %{buildroot}%{BIN_DIR}
%{__mkdir_p} %{buildroot}%{DOC_DIR}
%{__mkdir_p} %{buildroot}%{CONF_DIR}
%{__mkdir_p} %{buildroot}%{BIN_LINK}
%{__mkdir_p} %{buildroot}%{DOC_LINK}

%{__install} -p %{SOURCE1}  %{buildroot}%{BIN_DIR}/mansfor
%{__install} -p %{SOURCE2}  %{buildroot}%{BIN_DIR}/qmail-clam
%{__install} -p %{SOURCE3}  %{buildroot}%{BIN_DIR}/qmail-spam
%{__install} -p %{SOURCE4}  %{buildroot}%{BIN_DIR}/qmHandle
%{__install} -p %{SOURCE5}  %{buildroot}%{BIN_DIR}/qmlog
%{__install} -p %{SOURCE6}  %{buildroot}%{BIN_DIR}/qmqtool
%{__install} -p %{SOURCE7}  %{buildroot}%{BIN_DIR}/qt-backup
%{__install} -p %{SOURCE8}  %{buildroot}%{BIN_DIR}/qt-bootstrap-1
%{__install} -p %{SOURCE9}  %{buildroot}%{BIN_DIR}/qt-bootstrap-2
%{__install} -p %{SOURCE10} %{buildroot}%{BIN_DIR}/qt-config
%{__install} -p %{SOURCE11} %{buildroot}%{BIN_DIR}/qt-install
%{__install} -p %{SOURCE12} %{buildroot}%{BIN_DIR}/qt-install-dns-resolver
%{__install} -p %{SOURCE13} %{buildroot}%{BIN_DIR}/qt-install-epel
%{__install} -p %{SOURCE14} %{buildroot}%{BIN_DIR}/qt-install-repoforge
%{__install} -p %{SOURCE15} %{buildroot}%{BIN_DIR}/qt-mysql-secure-vpopmail
%{__install} -p %{SOURCE16} %{buildroot}%{BIN_DIR}/qt-prune-graylist
%{__install} -p %{SOURCE17} %{buildroot}%{BIN_DIR}/qt-restore
%{__install} -p %{SOURCE18} %{buildroot}%{BIN_DIR}/qt-setup-firewall
%{__install} -p %{SOURCE19} %{buildroot}%{BIN_DIR}/queue_repair.py
%{__install} -p %{SOURCE20} %{buildroot}%{BIN_DIR}/sa-stats

%{__install} -p %{SOURCE21} %{buildroot}%{CONF_DIR}/qmlog-trim.sed

%{__install} -p %{SOURCE22} %{buildroot}%{DOC_DIR}/artistic.txt
%{__install} -p %{SOURCE23} %{buildroot}%{DOC_DIR}/gpl.txt
%{__install} -p %{SOURCE24} %{buildroot}%{DOC_DIR}/licenses.txt
%{__install} -p %{SOURCE25} %{buildroot}%{DOC_DIR}/qmHandle.doc.txt
%{__install} -p %{SOURCE26} %{buildroot}%{DOC_DIR}/qmqtool.doc.txt
%{__install} -p %{SOURCE27} %{buildroot}%{DOC_DIR}/qmqtool.faq.txt
%{__install} -p %{SOURCE28} %{buildroot}%{DOC_DIR}/queue_repair.doc.txt

%{__ln_s} ../..%{BIN_DIR}/mansfor                   %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qmail-clam                %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qmail-spam                %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qmHandle                  %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qmlog                     %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qmqtool                   %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-backup                 %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-bootstrap-1            %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-bootstrap-2            %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-config                 %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-install                %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-install-dns-resolver   %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-install-epel           %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-install-repoforge      %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-mysql-secure-vpopmail  %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-prune-graylist         %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-restore                %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/qt-setup-firewall         %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/queue_repair.py           %{buildroot}%{BIN_LINK}/.
%{__ln_s} ../..%{BIN_DIR}/sa-stats                  %{buildroot}%{BIN_LINK}/.

%{__ln_s} ../..%{DOC_DIR}/artistic.txt              %{buildroot}%{DOC_LINK}/.
%{__ln_s} ../..%{DOC_DIR}/gpl.txt                   %{buildroot}%{DOC_LINK}/.
%{__ln_s} ../..%{DOC_DIR}/licenses.txt              %{buildroot}%{DOC_LINK}/.
%{__ln_s} ../..%{DOC_DIR}/qmHandle.doc.txt          %{buildroot}%{DOC_LINK}/.
%{__ln_s} ../..%{DOC_DIR}/qmqtool.doc.txt           %{buildroot}%{DOC_LINK}/.
%{__ln_s} ../..%{DOC_DIR}/qmqtool.faq.txt           %{buildroot}%{DOC_LINK}/.
%{__ln_s} ../..%{DOC_DIR}/queue_repair.doc.txt      %{buildroot}%{DOC_LINK}/.

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
%dir %{CONF_DIR}
%dir %{DOC_DIR}

# files
%attr(0755, root, root)  %{BIN_DIR}/*
%config(noreplace)       %{CONF_DIR}/*
                         %{DOC_DIR}/*

# symlinks
%{BIN_LINK}/*
%{DOC_LINK}/*

#-------------------------------------------------------------------------------
%post
#-------------------------------------------------------------------------------

#-------------------------------------------------------------------------------
%changelog
#-------------------------------------------------------------------------------
* Mon Apr 21 2014 Eric Shubert <eric@datamatters.us> - 2.0-1.qt
- Added qtp scripts, doc files
* Fri Feb  7 2014 Eric Shubert <eric@datamatters.us> - 2.0-0.qt
- Added qt-install-epel script
* Fri Dec 27 2013 Eric Shubert <eric@datamatters.us> - 1.0-0.qt
- Added qt-setup-firewall script
- Added qt-install-dns-resolver script
- Added qt-install script
* Sat Dec 21 2013 Eric Shubert <eric@datamatters.us> - 1.0-0.qt
- Added qt-mysql-secure-vpopmail script
* Mon Dec 16 2013 Eric Shubert <eric@datamatters.us> - 1.0-0.qt
- Initial package.
