%define upstream_name       Kwiki-Attachments
%define upstream_version    0.21

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Kwiki Page Attachments Plugin
License:    GPL
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Kwiki/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(Kwiki)
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{upstream_name}-%{upstream_version} 
rm -f ._Makefile.PL

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
#%{__make} test

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

