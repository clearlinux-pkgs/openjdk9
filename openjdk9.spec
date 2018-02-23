Name     : openjdk9
Version  : 9
Release  : 3
URL      : http://localhost/cgit/projects/jdk9/snapshot/jdk9.tar.gz
Source0  : http://localhost/cgit/projects/jdk9/snapshot/jdk9.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 Libpng MIT
BuildRequires : openjdk
BuildRequires : openjdk-dev
BuildRequires : zip
BuildRequires : libX11-dev
BuildRequires : libXtst-dev
BuildRequires : libXt-dev
BuildRequires : libXrender-dev
BuildRequires : libXi-dev
BuildRequires : libXext-dev
BuildRequires : xproto-dev
BuildRequires : xextproto-dev
BuildRequires : kbproto-dev
BuildRequires : renderproto-dev
BuildRequires : inputproto-dev
BuildRequires : cups-dev
BuildRequires : freetype-dev
BuildRequires : alsa-lib-dev
BuildRequires : ca-certs
BuildRequires : openssl-dev
BuildRequires : nss-dev
BuildRequires : glibc-bin
Requires : openjdk9-lib
Requires : openjdk9-bin
Requires : openjdk9-doc
Patch1   : 0001-openjdk9-rename-jli-as-jli9.patch

%description
OpenJDK (Open Java Development Kit) is a free and open source implementation of
the Java Platform, Standard Edition (Java SE).

%package bin
Summary: bin components for the openjdk9 package.
Group: Binaries
Requires : openjdk9-lib

%description bin
bin components for the openjdk9 package.

%package doc
Summary: doc components for the openjdk9 package.
Group: Documentation

%description doc
doc components for the openjdk9 package.

%package dev
Summary: dev components for the openjdk9 package.
Group: Development
Requires : openjdk9

%description dev
dev components for the openjdk9 package.

%package lib 
Summary: lib components for the openjdk9 package.
Group: Libraries 
Provides : libjli9.so()(64bit)
Provides : libjli9.so(SUNWprivate_1.1)(64bit)

%description lib
lib components for the openjdk9 package.

%prep
%setup -q -n jdk9
%patch1 -p1

%build
CLR_TRUST_STORE=%{_builddir}/trust-store clrtrust generate
bash configure CC=/usr/bin/gcc CXX=/usr/bin/g++ \
--disable-warnings-as-errors \
--with-boot-jdk=/usr/lib/jvm/java-1.8.0-openjdk \
--x-includes=/usr/include/ \
--x-libraries=/usr/lib64 \
--with-extra-cflags="-O3 $CFLAGS -fno-delete-null-pointer-checks -fno-guess-branch-probability -g1" \
--with-extra-cxxflags="$CXXFLAGS -std=gnu++98 -fno-delete-null-pointer-checks -fno-guess-branch-probability -g1" \
--with-zlib=system \
--enable-unlimited-crypto \
--with-cacerts-file=%{_builddir}/trust-store/compat/ca-roots.keystore \
--prefix=%{buildroot}/usr/lib

make images

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib/jvm/java-1.9.0-openjdk
cp -r build/linux-x86_64-normal-server-release/images/jdk/* %{buildroot}/usr/lib/jvm/java-1.9.0-openjdk

# Remove the copied keystore and link it to the runtime store
rm -f %{buildroot}/usr/lib/jvm/java-1.9.0-openjdk/lib/security/cacerts
ln -s /var/cache/ca-certs/compat/ca-roots.keystore %{buildroot}/usr/lib/jvm/java-1.9.0-openjdk/lib/security/cacerts

mkdir -p %{buildroot}/usr/lib64
ln -s /usr/lib/jvm/java-1.9.0-openjdk/lib/jli/libjli9.so %{buildroot}/usr/lib64/libjli9.so

mkdir -p %{buildroot}/usr/bin
# Basic binaries
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/java %{buildroot}/usr/bin/java9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jjs %{buildroot}/usr/bin/jjs9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/keytool %{buildroot}/usr/bin/keytool9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/orbd %{buildroot}/usr/bin/orbd9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/pack200 %{buildroot}/usr/bin/pack2009
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/policytool %{buildroot}/usr/bin/policytool9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/rmid %{buildroot}/usr/bin/rmid9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/rmiregistry %{buildroot}/usr/bin/rmiregistry9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/servertool %{buildroot}/usr/bin/servertool9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/tnameserv %{buildroot}/usr/bin/tnameserv9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/unpack200 %{buildroot}/usr/bin/unpack2009

# Dev binaries
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/appletviewer %{buildroot}/usr/bin/appletviewer9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/idlj %{buildroot}/usr/bin/idlj9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jar %{buildroot}/usr/bin/jar9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jarsigner %{buildroot}/usr/bin/jarsigner9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/javac %{buildroot}/usr/bin/javac9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/javadoc %{buildroot}/usr/bin/javadoc9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/javah %{buildroot}/usr/bin/javah9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/javap %{buildroot}/usr/bin/javap9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jcmd %{buildroot}/usr/bin/jcmd9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jconsole %{buildroot}/usr/bin/jconsole9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jdb %{buildroot}/usr/bin/jdb9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jdeprscan %{buildroot}/usr/bin/jdeprscan9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jdeps %{buildroot}/usr/bin/jdeps9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jhsdb %{buildroot}/usr/bin/jhsdb9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jimage %{buildroot}/usr/bin/jimage9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jinfo %{buildroot}/usr/bin/jinfo9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jlink %{buildroot}/usr/bin/jlink9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jmap %{buildroot}/usr/bin/jmap9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jmod %{buildroot}/usr/bin/jmod9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jps %{buildroot}/usr/bin/jps9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jrunscript %{buildroot}/usr/bin/jrunscript9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jshell %{buildroot}/usr/bin/jshell9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jstack %{buildroot}/usr/bin/jstack9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jstat %{buildroot}/usr/bin/jstat9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/jstatd %{buildroot}/usr/bin/jstatd9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/native2ascii %{buildroot}/usr/bin/native2ascii9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/rmic %{buildroot}/usr/bin/rmic9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/schemagen %{buildroot}/usr/bin/schemagen9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/serialver %{buildroot}/usr/bin/serialver9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/wsgen %{buildroot}/usr/bin/wsgen9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/wsimport %{buildroot}/usr/bin/wsimport9
ln -s /usr/lib/jvm/java-1.9.0-openjdk/bin/xjc %{buildroot}/usr/bin/xjc9

#%check
#make WARNINGS_ARE_ERRORS="-Wno-error" \
#CFLAGS_WARNINGS_ARE_ERRORS="-Wno-error" \
#run-test-tier1

%files
%defattr(-,root,root,-)
/usr/lib/jvm/java-1.9.0-openjdk/release
/usr/lib/jvm/java-1.9.0-openjdk/conf/logging.properties
/usr/lib/jvm/java-1.9.0-openjdk/conf/management/jmxremote.access
/usr/lib/jvm/java-1.9.0-openjdk/conf/management/jmxremote.password.template
/usr/lib/jvm/java-1.9.0-openjdk/conf/management/management.properties
/usr/lib/jvm/java-1.9.0-openjdk/conf/net.properties
/usr/lib/jvm/java-1.9.0-openjdk/conf/security/java.policy
/usr/lib/jvm/java-1.9.0-openjdk/conf/security/java.security
/usr/lib/jvm/java-1.9.0-openjdk/conf/security/policy/README.txt
/usr/lib/jvm/java-1.9.0-openjdk/conf/security/policy/limited/default_US_export.policy
/usr/lib/jvm/java-1.9.0-openjdk/conf/security/policy/limited/default_local.policy
/usr/lib/jvm/java-1.9.0-openjdk/conf/security/policy/limited/exempt_local.policy
/usr/lib/jvm/java-1.9.0-openjdk/conf/security/policy/unlimited/default_US_export.policy
/usr/lib/jvm/java-1.9.0-openjdk/conf/security/policy/unlimited/default_local.policy
/usr/lib/jvm/java-1.9.0-openjdk/conf/sound.properties
/usr/lib/jvm/java-1.9.0-openjdk/demo/README
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/ArcTest/ArcCanvas.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/ArcTest/ArcControls.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/ArcTest/ArcTest.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/ArcTest/ArcTest.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/ArcTest/IntegerTextField.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/ArcTest/example1.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/BarChart/BarChart.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/BarChart/BarChart.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/BarChart/example1.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/BarChart/example2.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/Blink/Blink$1.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/Blink/Blink.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/Blink/Blink.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/Blink/example1.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/CardTest/CardPanel.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/CardTest/CardTest.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/CardTest/CardTest.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/CardTest/example1.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/Clock/Clock.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/Clock/Clock.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/Clock/example1.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/DitherTest/CardinalTextField.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/DitherTest/DitherCanvas.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/DitherTest/DitherControls.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/DitherTest/DitherMethod.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/DitherTest/DitherTest$1.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/DitherTest/DitherTest.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/DitherTest/DitherTest.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/DitherTest/example1.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/DrawTest/DrawControls.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/DrawTest/DrawPanel.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/DrawTest/DrawTest.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/DrawTest/DrawTest.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/DrawTest/example1.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/Fractal/CLSFractal.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/Fractal/CLSFractal.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/Fractal/CLSRule.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/Fractal/CLSTurtle.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/Fractal/ContextLSystem.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/Fractal/example1.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/AppletFrame.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/AppletFrame.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/ArcCard.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/ArcDegreePanel.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/ArcPanel.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/ColorUtils.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/GraphicsCards.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/GraphicsPanel.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/GraphicsTest.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/GraphicsTest.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/OvalShape.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/PolygonShape.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/RectShape.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/RoundRectShape.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/Shape.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/ShapeTest.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/GraphicsTest/example1.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/MoleculeViewer/Matrix3D.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/MoleculeViewer/MoleculeViewer.jar
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/MoleculeViewer/XYZApp.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/MoleculeViewer/example1.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/MoleculeViewer/example2.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/MoleculeViewer/example3.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/MoleculeViewer/src.zip
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/NervousText/NervousText.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/NervousText/NervousText.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/NervousText/example1.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SimpleGraph/GraphApplet.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SimpleGraph/GraphApplet.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SimpleGraph/example1.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SortDemo/BidirBubbleSortAlgorithm.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SortDemo/BidirBubbleSortAlgorithm.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SortDemo/BubbleSortAlgorithm.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SortDemo/BubbleSortAlgorithm.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SortDemo/QSortAlgorithm.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SortDemo/QSortAlgorithm.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SortDemo/SortAlgorithm.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SortDemo/SortAlgorithm.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SortDemo/SortItem.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SortDemo/SortItem.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SortDemo/example1.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SpreadSheet/Cell.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SpreadSheet/CellUpdater.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SpreadSheet/InputField.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SpreadSheet/Node.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SpreadSheet/SpreadSheet.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SpreadSheet/SpreadSheet.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SpreadSheet/SpreadSheetInput.class
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/SpreadSheet/example1.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/WireFrame/Matrix3D.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/WireFrame/ThreeD.java
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/WireFrame/WireFrame.jar
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/WireFrame/example1.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/WireFrame/example2.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/WireFrame/example3.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/WireFrame/example4.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/applets/WireFrame/src.zip
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/CodePointIM/CodePointIM.jar
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/CodePointIM/README.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/CodePointIM/README_ja.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/CodePointIM/README_zh_CN.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/CodePointIM/src.zip
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/FileChooserDemo/FileChooserDemo.jar
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/FileChooserDemo/README.txt
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/FileChooserDemo/src.zip
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/Font2DTest/Font2DTest.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/Font2DTest/Font2DTest.jar
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/Font2DTest/README.txt
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/Font2DTest/src.zip
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/Metalworks/Metalworks.jar
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/Metalworks/README.txt
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/Metalworks/src.zip
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/Notepad/Notepad.jar
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/Notepad/README.txt
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/Notepad/src.zip
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/SampleTree/README.txt
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/SampleTree/SampleTree.jar
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/SampleTree/src.zip
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/SwingApplet/README.txt
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/SwingApplet/SwingApplet.html
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/SwingApplet/SwingApplet.jar
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/SwingApplet/src.zip
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/TableExample/README.txt
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/TableExample/TableExample.jar
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/TableExample/src.zip
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/TransparentRuler/README.txt
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/TransparentRuler/TransparentRuler.jar
/usr/lib/jvm/java-1.9.0-openjdk/demo/jfc/TransparentRuler/src.zip
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/README.txt
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/FileChooserDemo/build.properties
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/FileChooserDemo/build.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/FileChooserDemo/nbproject/file-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/FileChooserDemo/nbproject/jdk.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/FileChooserDemo/nbproject/netbeans-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/FileChooserDemo/nbproject/project.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Font2DTest/build.properties
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Font2DTest/build.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Font2DTest/nbproject/file-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Font2DTest/nbproject/jdk.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Font2DTest/nbproject/netbeans-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Font2DTest/nbproject/project.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Metalworks/build.properties
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Metalworks/build.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Metalworks/nbproject/file-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Metalworks/nbproject/jdk.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Metalworks/nbproject/netbeans-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Metalworks/nbproject/project.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Notepad/build.properties
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Notepad/build.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Notepad/nbproject/file-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Notepad/nbproject/jdk.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Notepad/nbproject/netbeans-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/Notepad/nbproject/project.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/SampleTree/build.properties
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/SampleTree/build.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/SampleTree/nbproject/file-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/SampleTree/nbproject/jdk.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/SampleTree/nbproject/netbeans-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/SampleTree/nbproject/project.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/SwingApplet/build.properties
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/SwingApplet/build.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/SwingApplet/nbproject/file-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/SwingApplet/nbproject/jdk.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/SwingApplet/nbproject/netbeans-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/SwingApplet/nbproject/project.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/TableExample/build.properties
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/TableExample/build.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/TableExample/nbproject/file-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/TableExample/nbproject/jdk.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/TableExample/nbproject/netbeans-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/TableExample/nbproject/project.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/TransparentRuler/build.properties
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/TransparentRuler/build.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/TransparentRuler/nbproject/file-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/TransparentRuler/nbproject/jdk.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/TransparentRuler/nbproject/netbeans-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/jfc/TransparentRuler/nbproject/project.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/FullThreadDump/build.properties
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/FullThreadDump/build.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/FullThreadDump/nbproject/file-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/FullThreadDump/nbproject/jdk.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/FullThreadDump/nbproject/netbeans-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/FullThreadDump/nbproject/project.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/JTop/build.properties
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/JTop/build.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/JTop/nbproject/file-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/JTop/nbproject/jdk.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/JTop/nbproject/netbeans-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/JTop/nbproject/project.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/MemoryMonitor/build.properties
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/MemoryMonitor/build.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/MemoryMonitor/nbproject/file-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/MemoryMonitor/nbproject/jdk.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/MemoryMonitor/nbproject/netbeans-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/MemoryMonitor/nbproject/project.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/VerboseGC/build.properties
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/VerboseGC/build.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/VerboseGC/nbproject/file-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/VerboseGC/nbproject/jdk.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/VerboseGC/nbproject/netbeans-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/management/VerboseGC/nbproject/project.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/project.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/scripting/jconsole-plugin/build.properties
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/scripting/jconsole-plugin/build.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/scripting/jconsole-plugin/nbproject/file-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/scripting/jconsole-plugin/nbproject/jdk.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/scripting/jconsole-plugin/nbproject/netbeans-targets.xml
/usr/lib/jvm/java-1.9.0-openjdk/demo/nbproject/scripting/jconsole-plugin/nbproject/project.xml
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.activation.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.base.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.compiler.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.corba.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.datatransfer.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.desktop.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.instrument.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.logging.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.management.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.management.rmi.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.naming.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.prefs.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.rmi.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.scripting.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.se.ee.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.se.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.security.jgss.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.security.sasl.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.smartcardio.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.sql.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.sql.rowset.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.transaction.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.xml.bind.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.xml.crypto.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.xml.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.xml.ws.annotation.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/java.xml.ws.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.accessibility.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.attach.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.charsets.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.compiler.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.crypto.cryptoki.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.crypto.ec.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.dynalink.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.editpad.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.hotspot.agent.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.httpserver.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.incubator.httpclient.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.internal.ed.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.internal.jvmstat.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.internal.le.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.internal.opt.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.internal.vm.ci.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.jartool.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.javadoc.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.jcmd.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.jconsole.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.jdeps.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.jdi.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.jdwp.agent.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.jlink.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.jshell.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.jsobject.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.jstatd.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.localedata.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.management.agent.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.management.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.naming.dns.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.naming.rmi.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.net.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.pack.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.policytool.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.rmic.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.scripting.nashorn.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.scripting.nashorn.shell.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.sctp.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.security.auth.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.security.jgss.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.unsupported.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.xml.bind.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.xml.dom.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.xml.ws.jmod
/usr/lib/jvm/java-1.9.0-openjdk/jmods/jdk.zipfs.jmod
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.activation/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.activation/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.base/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.base/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.base/aes.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.base/asm.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.base/cldr.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.base/icu.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.base/zlib.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.compiler/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.compiler/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.corba/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.corba/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.datatransfer/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.datatransfer/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.desktop/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.desktop/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.desktop/colorimaging.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.desktop/fontconfig.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.desktop/giflib.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.desktop/harfbuzz.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.desktop/jpeg.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.desktop/lcms.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.desktop/libpng.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.desktop/mesa3d.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.desktop/opengl.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.desktop/xwindows.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.instrument/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.instrument/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.logging/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.logging/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.management.rmi/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.management.rmi/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.management/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.management/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.naming/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.naming/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.prefs/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.prefs/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.rmi/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.rmi/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.scripting/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.scripting/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.se.ee/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.se.ee/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.se/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.se/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.security.jgss/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.security.jgss/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.security.sasl/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.security.sasl/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.smartcardio/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.smartcardio/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.smartcardio/pcsclite.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.sql.rowset/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.sql.rowset/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.sql/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.sql/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.transaction/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.transaction/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml.bind/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml.bind/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml.crypto/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml.crypto/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml.crypto/santuario.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml.ws.annotation/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml.ws.annotation/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml.ws/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml.ws/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml/bcel.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml/dom.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml/jcup.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml/xalan.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml/xerces.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/java.xml/xmlresolver.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.accessibility/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.accessibility/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.attach/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.attach/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.charsets/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.charsets/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.compiler/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.compiler/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.crypto.cryptoki/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.crypto.cryptoki/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.crypto.cryptoki/pkcs11cryptotoken.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.crypto.cryptoki/pkcs11wrapper.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.crypto.ec/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.crypto.ec/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.crypto.ec/ecc.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.dynalink/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.dynalink/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.dynalink/dynalink.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.editpad/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.editpad/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.hotspot.agent/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.hotspot.agent/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.httpserver/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.httpserver/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.incubator.httpclient/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.incubator.httpclient/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.internal.ed/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.internal.ed/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.internal.jvmstat/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.internal.jvmstat/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.internal.le/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.internal.le/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.internal.le/jline.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.internal.opt/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.internal.opt/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.internal.opt/jopt-simple.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.internal.vm.ci/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.internal.vm.ci/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jartool/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jartool/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.javadoc/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.javadoc/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.javadoc/jquery.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.javadoc/jszip.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.javadoc/pako.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jcmd/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jcmd/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jconsole/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jconsole/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jdeps/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jdeps/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jdi/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jdi/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jdwp.agent/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jdwp.agent/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jlink/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jlink/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jshell/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jshell/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jsobject/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jsobject/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jstatd/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.jstatd/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.localedata/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.localedata/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.localedata/cldr.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.localedata/thaidict.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.management.agent/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.management.agent/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.management/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.management/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.naming.dns/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.naming.dns/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.naming.rmi/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.naming.rmi/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.net/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.net/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.pack/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.pack/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.policytool/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.policytool/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.rmic/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.rmic/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.scripting.nashorn.shell/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.scripting.nashorn.shell/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.scripting.nashorn/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.scripting.nashorn/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.scripting.nashorn/double-conversion.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.scripting.nashorn/joni.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.sctp/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.sctp/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.security.auth/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.security.auth/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.security.jgss/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.security.jgss/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.unsupported/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.unsupported/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.xml.bind/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.xml.bind/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.xml.bind/freebxml.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.xml.bind/relaxngdatatype.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.xml.bind/rngom.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.xml.bind/xmlresolver.md
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.xml.dom/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.xml.dom/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.xml.ws/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.xml.ws/LICENSE
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.zipfs/ASSEMBLY_EXCEPTION
/usr/lib/jvm/java-1.9.0-openjdk/legal/jdk.zipfs/LICENSE


%files bin
%defattr(-,root,root,-)
/usr/bin/java9
/usr/bin/jjs9
/usr/bin/keytool9
/usr/bin/orbd9
/usr/bin/pack2009
/usr/bin/policytool9
/usr/bin/rmid9
/usr/bin/rmiregistry9
/usr/bin/servertool9
/usr/bin/tnameserv9
/usr/bin/unpack2009
/usr/lib/jvm/java-1.9.0-openjdk/bin/java
/usr/lib/jvm/java-1.9.0-openjdk/bin/jjs
/usr/lib/jvm/java-1.9.0-openjdk/bin/keytool
/usr/lib/jvm/java-1.9.0-openjdk/bin/orbd
/usr/lib/jvm/java-1.9.0-openjdk/bin/pack200
/usr/lib/jvm/java-1.9.0-openjdk/bin/policytool
/usr/lib/jvm/java-1.9.0-openjdk/bin/rmid
/usr/lib/jvm/java-1.9.0-openjdk/bin/rmiregistry
/usr/lib/jvm/java-1.9.0-openjdk/bin/servertool
/usr/lib/jvm/java-1.9.0-openjdk/bin/tnameserv
/usr/lib/jvm/java-1.9.0-openjdk/bin/unpack200


%files lib
%defattr(-,root,root,-)
/usr/lib/jvm/java-1.9.0-openjdk/lib/classlist
/usr/lib/jvm/java-1.9.0-openjdk/lib/ct.sym
/usr/lib/jvm/java-1.9.0-openjdk/lib/jexec
/usr/lib/jvm/java-1.9.0-openjdk/lib/jexec.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/jli/libjli9.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/jli/libjli9.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/jrt-fs.jar
/usr/lib/jvm/java-1.9.0-openjdk/lib/jvm.cfg
/usr/lib/jvm/java-1.9.0-openjdk/lib/libattach.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libattach.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libawt.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libawt.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libawt_headless.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libawt_headless.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libawt_xawt.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libawt_xawt.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libdt_socket.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libdt_socket.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libfontmanager.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libfontmanager.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libinstrument.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libinstrument.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libj2gss.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libj2gss.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libj2pcsc.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libj2pcsc.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libj2pkcs11.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libj2pkcs11.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjaas_unix.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjaas_unix.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjava.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjava.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjavajpeg.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjavajpeg.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjawt.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjawt.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjdwp.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjdwp.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjimage.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjimage.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjsig.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjsig.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjsound.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjsound.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjsoundalsa.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libjsoundalsa.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/liblcms.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/liblcms.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libmanagement.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libmanagement.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libmanagement_agent.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libmanagement_agent.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libmanagement_ext.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libmanagement_ext.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libmlib_image.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libmlib_image.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libnet.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libnet.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libnio.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libnio.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libprefs.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libprefs.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/librmi.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/librmi.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libsaproc.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libsaproc.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libsctp.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libsctp.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libsplashscreen.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libsplashscreen.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libsunec.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libsunec.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libunpack.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libunpack.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libverify.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libverify.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/libzip.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/libzip.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/modules
/usr/lib/jvm/java-1.9.0-openjdk/lib/psfont.properties.ja
/usr/lib/jvm/java-1.9.0-openjdk/lib/psfontj2d.properties
/usr/lib/jvm/java-1.9.0-openjdk/lib/security/blacklisted.certs
/usr/lib/jvm/java-1.9.0-openjdk/lib/security/cacerts
/usr/lib/jvm/java-1.9.0-openjdk/lib/security/default.policy
/usr/lib/jvm/java-1.9.0-openjdk/lib/server/Xusage.txt
/usr/lib/jvm/java-1.9.0-openjdk/lib/server/libjsig.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/server/libjsig.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/server/libjvm.diz
/usr/lib/jvm/java-1.9.0-openjdk/lib/server/libjvm.so
/usr/lib/jvm/java-1.9.0-openjdk/lib/src.zip
/usr/lib/jvm/java-1.9.0-openjdk/lib/tzdb.dat
/usr/lib64/libjli9.so

%files dev
%defattr(-,root,root,-)
/usr/bin/appletviewer9
/usr/bin/idlj9
/usr/bin/jar9
/usr/bin/jarsigner9
/usr/bin/javac9
/usr/bin/javadoc9
/usr/bin/javah9
/usr/bin/javap9
/usr/bin/jcmd9
/usr/bin/jconsole9
/usr/bin/jdb9
/usr/bin/jdeprscan9
/usr/bin/jdeps9
/usr/bin/jhsdb9
/usr/bin/jimage9
/usr/bin/jinfo9
/usr/bin/jlink9
/usr/bin/jmap9
/usr/bin/jmod9
/usr/bin/jps9
/usr/bin/jrunscript9
/usr/bin/jshell9
/usr/bin/jstack9
/usr/bin/jstat9
/usr/bin/jstatd9
/usr/bin/native2ascii9
/usr/bin/rmic9
/usr/bin/schemagen9
/usr/bin/serialver9
/usr/bin/wsgen9
/usr/bin/wsimport9
/usr/bin/xjc9
/usr/lib/jvm/java-1.9.0-openjdk/bin/appletviewer
/usr/lib/jvm/java-1.9.0-openjdk/bin/idlj
/usr/lib/jvm/java-1.9.0-openjdk/bin/jar
/usr/lib/jvm/java-1.9.0-openjdk/bin/jarsigner
/usr/lib/jvm/java-1.9.0-openjdk/bin/javac
/usr/lib/jvm/java-1.9.0-openjdk/bin/javadoc
/usr/lib/jvm/java-1.9.0-openjdk/bin/javah
/usr/lib/jvm/java-1.9.0-openjdk/bin/javap
/usr/lib/jvm/java-1.9.0-openjdk/bin/jcmd
/usr/lib/jvm/java-1.9.0-openjdk/bin/jconsole
/usr/lib/jvm/java-1.9.0-openjdk/bin/jdb
/usr/lib/jvm/java-1.9.0-openjdk/bin/jdeprscan
/usr/lib/jvm/java-1.9.0-openjdk/bin/jdeps
/usr/lib/jvm/java-1.9.0-openjdk/bin/jhsdb
/usr/lib/jvm/java-1.9.0-openjdk/bin/jimage
/usr/lib/jvm/java-1.9.0-openjdk/bin/jinfo
/usr/lib/jvm/java-1.9.0-openjdk/bin/jlink
/usr/lib/jvm/java-1.9.0-openjdk/bin/jmap
/usr/lib/jvm/java-1.9.0-openjdk/bin/jmod
/usr/lib/jvm/java-1.9.0-openjdk/bin/jps
/usr/lib/jvm/java-1.9.0-openjdk/bin/jrunscript
/usr/lib/jvm/java-1.9.0-openjdk/bin/jshell
/usr/lib/jvm/java-1.9.0-openjdk/bin/jstack
/usr/lib/jvm/java-1.9.0-openjdk/bin/jstat
/usr/lib/jvm/java-1.9.0-openjdk/bin/jstatd
/usr/lib/jvm/java-1.9.0-openjdk/bin/rmic
/usr/lib/jvm/java-1.9.0-openjdk/bin/schemagen
/usr/lib/jvm/java-1.9.0-openjdk/bin/serialver
/usr/lib/jvm/java-1.9.0-openjdk/bin/wsgen
/usr/lib/jvm/java-1.9.0-openjdk/bin/wsimport
/usr/lib/jvm/java-1.9.0-openjdk/bin/xjc
/usr/lib/jvm/java-1.9.0-openjdk/include/classfile_constants.h
/usr/lib/jvm/java-1.9.0-openjdk/include/ir.idl
/usr/lib/jvm/java-1.9.0-openjdk/include/jawt.h
/usr/lib/jvm/java-1.9.0-openjdk/include/jdwpTransport.h
/usr/lib/jvm/java-1.9.0-openjdk/include/jni.h
/usr/lib/jvm/java-1.9.0-openjdk/include/jvmti.h
/usr/lib/jvm/java-1.9.0-openjdk/include/jvmticmlr.h
/usr/lib/jvm/java-1.9.0-openjdk/include/linux/jawt_md.h
/usr/lib/jvm/java-1.9.0-openjdk/include/linux/jni_md.h
/usr/lib/jvm/java-1.9.0-openjdk/include/orb.idl

%files doc
%defattr(-,root,root,-)
/usr/lib/jvm/java-1.9.0-openjdk/man/ja
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/appletviewer.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/idlj.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/jar.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/jarsigner.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/java.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/javac.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/javadoc.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/javah.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/javap.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/jcmd.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/jconsole.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/jdb.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/jdeps.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/jinfo.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/jjs.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/jmap.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/jps.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/jrunscript.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/jstack.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/jstat.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/jstatd.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/keytool.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/orbd.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/pack200.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/policytool.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/rmic.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/rmid.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/rmiregistry.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/schemagen.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/serialver.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/servertool.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/tnameserv.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/unpack200.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/wsgen.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/wsimport.1
/usr/lib/jvm/java-1.9.0-openjdk/man/ja_JP.UTF-8/man1/xjc.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/appletviewer.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/idlj.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/jar.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/jarsigner.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/java.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/javac.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/javadoc.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/javah.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/javap.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/jcmd.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/jconsole.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/jdb.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/jdeps.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/jinfo.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/jjs.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/jmap.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/jps.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/jrunscript.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/jstack.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/jstat.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/jstatd.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/keytool.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/orbd.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/pack200.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/policytool.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/rmic.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/rmid.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/rmiregistry.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/schemagen.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/serialver.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/servertool.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/tnameserv.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/unpack200.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/wsgen.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/wsimport.1
/usr/lib/jvm/java-1.9.0-openjdk/man/man1/xjc.1

