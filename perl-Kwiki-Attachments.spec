%define module	Kwiki-Attachments
%define name	perl-%{module}
%define version 0.18
%define release %mkrel 4

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Kwiki Page Attachments Plugin
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Kwiki/%{module}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{module}/
License:	GPL
Group:		Development/Perl
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Kwiki)
BuildArch:	noarch

%description
Kwiki::Attachments gives a Kwiki wiki the ability to upload, store and manage
file attachments on any page. By default, if you have an image creation module
such as Imager or Image::Magick installed, then a thumbnail will be created for
every supported image file type that is uploaded. Thumbnails are displayed on
the attachments page, and can also be displayed on wiki pages via the wafl
directives described in the next paragraph. The thumbnail files have "thumb_"
prepended to the original filename and are not displayed separately in the
attachment page or widget. For this reason, you cannot upload files beginning
with "thumb_".

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Kwiki
%{_mandir}/*/*

