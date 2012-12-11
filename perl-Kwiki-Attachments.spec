%define upstream_name       Kwiki-Attachments
%define upstream_version    0.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Kwiki Page Attachments Plugin
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Kwiki/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
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
%setup -q -n %{upstream_name}-%{upstream_version} 
rm -f ._Makefile.PL

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#%{__make} test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Kwiki
%{_mandir}/*/*

%changelog
* Fri Jul 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.210.0-1mdv2010.0
+ Revision: 396752
- update to 0.21

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.200.0-1mdv2010.0
+ Revision: 389941
- new version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.18-7mdv2009.0
+ Revision: 257393
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.18-6mdv2009.0
+ Revision: 245414
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-4mdv2008.1
+ Revision: 133634
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-3mdv2007.0
- Rebuild

* Mon Apr 24 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-2mdk
- better sources URL
- better buildrequires syntax

* Thu Jan 19 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdk
- first mandriva release

