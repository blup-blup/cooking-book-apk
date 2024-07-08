import flet as ft

def main(page: ft.Page):
    page.title = "Cooking Book"
    page.theme_mode = ft.ThemeMode.DARK
  
    theme = ft.Theme()
    theme.page_transitions.windows = ft.PageTransitionTheme.NONE
    theme.page_transitions.android = ft.PageTransitionTheme.NONE
    theme.page_transitions.macos = ft.PageTransitionTheme.NONE
    theme.page_transitions.ios = ft.PageTransitionTheme.NONE
    page.theme = theme

    AppBar = ft.AppBar(    
        title=ft.Text('Cooking Book', weight=ft.FontWeight.BOLD, size=18, color=ft.colors.WHITE),
        bgcolor=ft.colors.BLACK,
        automatically_imply_leading=True

    )

    makanan = ft.ListView(
        padding=ft.padding.only(5, 5, 5, 5),
        expand=True,
        controls=[
            ft.Column(
                spacing=30,
                controls=[
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/ayam-geprek.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Ayam geprek', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/ayam-geprek')
                                        )
                                    ]
                            ),
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/ayam-taliwang.webp',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Ayam taliwang', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/ayam-taliwang')
                                        )
                                    ]
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/bakmi.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Bakmi', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/bakmi')
                                        )
                                    ]
                            ),
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/bakso.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Bakso', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/bakso')
                                        )
                                    ]
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/batagor.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Batagor', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/batagor')
                                        )
                                    ]
                            ),
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/bubur-ayam.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Bubur ayam', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/bubur-ayam')
                                        )
                                    ]
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/empal-gentong.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Empal gentong', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/empal-gentong')
                                        )
                                    ]
                            ),
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/gado-gado.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Gado gado', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/gado-gado')
                                        )
                                    ]
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/gudeg.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Gudeg', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/gudeg')
                                        )
                                    ]
                            ),
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/karedok.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Karedok', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/karedok')
                                        )
                                    ]
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/kolak.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Kolak', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/kolak')
                                        )
                                    ]
                            ),
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/ketoprak.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Ketoprak', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/ketoprak')
                                        )
                                    ]
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/martabak.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Martabak', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/martabak')
                                        )
                                    ]
                            ),
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/mie-aceh.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Mie aceh', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/mie-aceh')
                                        )
                                    ]
                            ),
                        ]
                    ),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.SPACE_AROUND,
                        controls=[
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/nasi-kuning.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Nasi kuning', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/nasi-kuning')
                                        )
                                    ]
                            ),
                            ft.Stack(
                                controls=[
                                    ft.Container(
                                        height=150,
                                        width=150,
                                        image_src='makanan/nasi-goreng.jpg',
                                        image_fit=ft.ImageFit.COVER,
                                        border_radius=10
                                    ),
                                    ft.Container(
                                        height=180,
                                        width=150,
                                        border_radius=10,
                                        content=ft.Text('Nasi goreng', weight=ft.FontWeight.BOLD, size=18),
                                        alignment=ft.alignment.bottom_center,
                                        ink=True,
                                        ink_color=ft.colors.WHITE,
                                        on_click=lambda _: page.go('/nasi-goreng')
                                        )
                                    ]
                            ),
                        ]
                    )
                ]
            )
        ]
    )

    def destination(e):
        if e.control.selected_index == 0:
            page.go('/')
        elif e.control.selected_index == 1:
            page.go('/about')

    Navbar = ft.CupertinoNavigationBar(
        bgcolor=ft.colors.BLACK,
        inactive_color=ft.colors.GREY,
        active_color=ft.colors.WHITE,
        on_change=destination,
        destinations=[
            ft.NavigationDestination(icon=ft.icons.HOME, label="Home"),
            ft.NavigationDestination(icon=ft.icons.INFO, label="About"),
        ]
    )

    def route_change(route):
        page.views.clear()
        page.views.append(
            ft.View(
                route="/",
                padding=20,
                spacing=0,
                controls=[
                    AppBar,
                    makanan,
                    Navbar
                ],
            )
        ),
        if page.route =='/about':
            page.views.clear()
            page.views.append(
                ft.View(
                    route="/about",
                    padding=20,
                    spacing=0,
                    controls=[
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    controls=[
                                        ft.ResponsiveRow(
                                            controls=[
                                                ft.Container(
                                                    # width=350,
                                                    content=ft.Text('My Profile', weight=ft.FontWeight.BOLD, size=18),
                                                    alignment=ft.alignment.top_center
                                                )
                                            ]
                                        ),
                                        ft.Divider(height=10),
                                        ft.ResponsiveRow(
                                            controls=[
                                                ft.Container(
                                                    image_src='makanan/gojo.png',
                                                    height=100,
                                                    width=100
                                                ),
                                                ft.Container(
                                                    content=ft.Text('Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'),
                                                    width=250,
                                                    alignment=ft.alignment.center
                                                )
                                            ]
                                        ),
                                        ft.Divider(height=100, color=ft.colors.TRANSPARENT),
                                        ft.ResponsiveRow(
                                            controls=[
                                                ft.Container(
                                                    content=ft.Text('Follow Media Sosial Saya', weight=ft.FontWeight.BOLD, size=18),
                                                    width=350,
                                                    alignment=ft.alignment.center
                                                )
                                            ]
                                        ),
                                        ft.Divider(height=5, color=ft.colors.TRANSPARENT),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Container(
                                                    image_src='makanan/logo-instagram.png',
                                                    height=50,
                                                    width=50,
                                                    ink=True,
                                                    url='https://www.instagram.com/mhmdaari.f?igsh=MWVidjh2andiM2JqaQ=='
                                                ),
                                                ft.Container(
                                                    image_src='makanan/whatsapp.png',
                                                    height=50,
                                                    width=50,
                                                    ink=True,
                                                    url='https://wa.me/qr/GCCLSGXLN3K7M1'
                                                )
                                            ]
                                        )
                                    ]
                                )
                            ]
                        ),
                        Navbar
                    ],
                )
            ),
        elif page.route == "/ayam-geprek":
            page.views.append(
                ft.View(
                    route="/ayam-geprek",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/ayam-geprek.jpg',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Ayam geprek', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan bahan:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 500 gram daging ayam (potong 4 bagian)\n2. 1/2 sdt air jeruk nipis\n3. 700 ml air es\n4. 150 gram tepung terigu protein tinggi\n5. 1,5 sdt baking powder\n6. 30 gram tepung maizena\n7. Garam dan merica secukupnya'),
                                                height=150,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. Pertama, lumuri ayam dengan air jeruk nipis, garam dan merica. Marinasi sekitar 30 menit dalam lemari es.\n2. Kedua, campurkan tepung, baking powder, tepung maizena, garam dan lada dalam satu wadah.\n3. Ketiga, gulingkan ayam ke dalam campuran tepung dan celupkan daging ayam ke dalam air es. Gulingkan ke dalam campuran tepung lagi sambil agak ditekan dan diangkat. Ulangi satu kali lagi.\n4. Keempat, panaskan minyak dan goreng ayam yang sudah dibalutkan dengan tepung hingga matang dan kecokelatan, angkat.\n5. Dan terakhir, ayam goreng tepung siap digeprek dengan sambal kesukaan kamu.'),
                                                height=400,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        elif page.route == "/ayam-taliwang":
            page.views.append(
                ft.View(
                    route="/ayam-taliwang",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/ayam-taliwang.webp',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Ayam taliwang', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan :', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 1 ekor ayam kampung, belah dua tidak putus, tekan sedikit supaya melebar\n2. 2 sendok teh air jeruk limau\n3. 1 sendok teh garam\n4. 750 ml santan dari 1/2 butir kelapa\n5. 3 sendok teh garam\n6. 2 sendok makan gula merah sisir\n7. 5 sendok makan minyak untuk menumis'),
                                                height=180,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan basah :', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 10 butir bawang merah, bakar\n2. 5 siung bawang putih, bakar\n3. 4 buah cabai merah besar, bakar\n4. 6 buah cabai merah keriting, bakar\n5. 5 butir kemiri, sangria\n6. 1 sendok teh terasi, bakar'),
                                                height=150,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. Lumuri ayam dengan air jeruk limau dan garam. Bakar sampai setengah matang.\n2. Panaskan minyak. Tumis bumbu halus sampai harum. Masukkan santan, garam, dan gula merah. Masak sampai mendidih.\n3. Tambahkan ayam. Masak dengan api kecil sampai matang dan meresap.\n4. Bakar lagi ayam sambil dioles sisa bumbu sampai harum.'),
                                                height=300,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        elif page.route == "/bakmi":
            page.views.append(
                ft.View(
                    route="/bakmi",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/bakmi.jpg',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Bakmi', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan bakmi:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 300 gram mi telur kering, rebus, sisihkan\n2. 1 ikat sawi hijau, potong besar, rebus\n3. 300 gram ayam filet, potong dadu100 gram jamur kancing, belah 2\n4. 1 buah bawang bombai ukuran kecil, cincang\n5. 2sdm saus tiram\n6. 2 sdm saus tiram\n7. 4 sdm kecap manis\n8. 1 sdt minyak wijen 100 ml air\n9. Garam, merica, dan kaldu jamur sesuai selera\n10. 2 sdm margarin'),
                                                height=220,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan minyak ayam bawang:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 150 gram kulit ayam\n2. 100ml minyak\n3. 6 siung bawang putih, cincang'),
                                                height=70,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan lain:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. kecap asin\n2. bakso kuah\n3. daun bawang, iris\n4. bawang goreng\n5. sambal rawit'),
                                                height=80,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. Lelehkan margarin. Tumis bawang bombai dan bawang putih sampai wangi. Masukkan ayam filet dan jamur. Masak sampai ayam berubah warna dan jamur layu.\n2. Masukkan saus tiram, kecap manis, minyak wijen, air, garam, merica, dan kaldu jamur. Masak sampai air surut dan bumbu meresap. Siap digunakan.\n3. Minyak ayam bawang: Panaskan minyak. Goreng kulit ayam dengan api kecil sampai garing. Angkat kulit ayam.\n4. Masukkan bawang putih cincang. Masak sampai bawang berwarna kekuningan. Matikan api. Dinginkan.\n5. Penyelesaian: aduk dua sendok makan minyak ayam bawang dan satu sendok makan kecap asin. Masukkan 1/4 bagian mi yang sudah direbus. Aduk sampai tercampur rata.\n6. Beri topping ayam jamur dan sayuran. Taburi dengan daun bawang dan bawang goreng. Sajikan dengan bakso kuah dan sambal rawit.'),
                                                height=500,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        elif page.route == "/bakso":
            page.views.append(
                ft.View(
                    route="/bakso",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/bakso.jpg',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Bakso', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan bakso:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 700 gram dada ayam tanpa kulit, cuci bersih, potong-potong\n2. 3 siung bawang putih, haluskan\n3. 70 gram tepung sagu\n4. 1 butir telur ayam\n5. 1/2 sdt bubuk merica halus\n6. 1 sdt baking powder\n7. 1 sdm minyak wijen\n8. 3 sdt garam\n9. 1 sdt gula pasir\n10. 100 ml air es\n11. 1.500 ml air untuk merebus bakso'),
                                                height=240,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Kuah bakso ayam:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 500 gram tulang ayam\n2. 2.000 ml air\n3. 4 siung bawang putih, cincang halus\n4. 1/2 sdt merica bubuk\n5. 2 sdt garam\n6. 1 sdt gula pasir7. 1 sdm kecap asin\n8. 2 sdm minyak goreng'),
                                                height=150,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat bakso ayam:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. Rebus air di dalam panci hingga mendidih dengan menggunakan api sedang. Jika sudah mendidih, kecilkan apinya.\n2. Masukkan dada ayam, bawang putih, tepung sagu, telur ayam, merica, baking powder, garam, gula pasir, dan air es ke dalam food processor.\n3. Proses sampai daging ayam menjadi adonan yang halus selama lebih kurang sekitar tiga menit. Jangan terlalu lama karena akan menyebabkan permukaan bakso menjadi kasar dan tidak mulus.\n4. Adonan siap dibentuk menjadi bulatan. Ambil sedikit adonan yang diletakkan di telapak tangan, tekan hingga adonan muncul di antara ibu jari dan telunjuk.\n5. Ambil pakai sendok makan, masukkan ke dalam air mendidih. Lakukan sampai adonan habis. Kalau bakso sudah mengapung berarti sudah matang. Angkat dan tiriskan. Sisihkan.'),
                                                height=350,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat kuah bakso ayam:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. Rebus air di dalam panci hingga mendidih di atas api sedang. Masukkan tulang ayam.\n2. Panaskan dua sendok makan minyak goreng. Tumis bawang putih cincang hingga harum dan berwarna kecoklatan. Masukkan tumisan bawang putih ke dalam kuah bakso ayam.\n3. Masukkan bakso ayam ke dalam kuah. Tambahkan merica bubuk, garam, gula pasir, dan kecap asin. Aduk rata. Masak sekitar 20 menit. Bakso ayam siap disajikan.'),
                                                height=300,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        elif page.route == "/batagor":
            page.views.append(
                ft.View(
                    route="/batagor",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/batagor.jpg',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Batagor', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan bahan:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 15 lembar kulit pangsit\n2. 5 buah tahu putih ukuran kecil, dibelah dua segitiga, di keruk tengahnya\n3. minyak untuk menggoreng\n4. 300 gram ikan tenggiri, haluskan\n5. 3 buah daun bawang, iris tipis\n6. 3 siung bawang putih, haluskan\n7. 1/2 sendok teh penyedap rasa\n8. 1 sendok teh garam\n9. 1/4 sendok teh merica bubuk\n10. 2 sendok teh gula pasir\n11. 3 putih telur\n12. 150 ml air es\n13. 150 gram tepung sagu\n14. 25 gram tepung terigu protein sedang'),
                                                height=300,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan sambal kacang:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 200 gram kacang tanah kulit goreng\n2. 5 siung bawang putih, goreng\n3. 6 buah cabai merah keriting, goreng\n4. 5 sendok makan gula merah\n5. 1/2 sendok makan garam\n6. 650 ml air hangat\n7. 2 sendok makan air asam jawa (dari 1 sendok makan asam jawa dilarutkan dalam 2 sendok makan air)'),
                                                height=170,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. Campur ikan tenggiri yang sudah dihaluskan dengan daun bawang, bawang putih, penyedap rasa, garam, merica bubuk, dan gula pasir. Masukkan dalam chopper. Blender supaya lebih halus dan tercampur rata.\n2. Masukkan putih telur dan air es. Blender kembali. Lalu tambahkan tepung sagu dan tepung terigu. Blender sampai tercampur rata.\n3. Bagi menjadi 2 adonan. Satu bagian isi ke dalam tahu putih. Sisanya masukkan dalam kulit pangsit. Rekatkan sisi kulit pangsit dengan air. Bentuk segi empat.\n4. Panaskan kukusan. Kukus adonan selama 30 menit dengan api sedang sampai matang. Dinginkan.\n5. Setelah dingin, goreng siomay dan batagor dalam minyak yang sudah dipanaskan dengan api sedang sampai matang. Tiriskan.\n6. Sambal kacang: haluskan kacang tanah, bawang putih, cabai merah keriting, gula merah, dan garam. Tambahkan air hangat dan aduk rata. Lalu masak sambal kacang sambil diaduk sampai kental. Setelah mengental, tambahkan air asam Jawa. Aduk rata. Matikan api.\n7. Sajikan batagor dengan siraman sambal kacang dan bahan pelengkapnya.'),
                                                height=550,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        elif page.route == "/bubur-ayam":
            page.views.append(
                ft.View(
                    route="/bubur-ayam",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/bubur-ayam.jpg',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Bubur ayam', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan bahan:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 1 canting beras ukuran rata-rata gelas takar yang ada di magic jar\n2. 1/2 sdm bubuk tabur mie goreng\n3. 1/2 sdt merica bubuk\n4. 1/2 sdt garam'),
                                                height=100,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Topping:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 1/2 sdt bubuk tabur mie goreng\n2. 1 sdm ayam suir\n3. kecap manis\n4. kecap asin\n5, kerupuk\n6. seledri'),
                                                height=120,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. cuci beras, beri air. masak sampai air surut dan beras telah pecah. masukan semua bumbu-bumbu. aduk-aduk sampai rata\n2. ambil bubur dimangkuk, beri kecap asin, kecap manis, bumbu mie goreng dan merica\n3. beri topping ayam suir, kerupuk dan seledri. siap dihidangkan'),
                                                height=250,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        elif page.route == "/empal-gentong":
            page.views.append(
                ft.View(
                    route="/empal-gentong",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/empal-gentong.jpg',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Empal gentong', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 500 gram daging sapi\n2. 500 gram jeroan sapi\n3. 1 liter santan sedang\n4. 1,5 liter air untuk merebus daging\n5. 2 lembar daun salam\n6. 2 batang serai, memarkan\n7. 4 cm kunyit, bakar\n8. 4 cm jahe, bakar\n9. 2 butir kapulaga\n10. 2 butir cengkih\n11. 1 ruas jempol lengkuas, memarkan\n12. 1 cm kayu manis\n13. garam, gula, dan kaldu sapi bubuk secukupnya'),
                                                height=270,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bumbu halus:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 10 butir bawang merah\n2. 6 siung bawang putih\n3. 4 butir kemiri, sangrai\n4. 2 cm jahe\n5. 1sdt merica butiran'),
                                                height=100,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan pelengkap:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. cabai bubuk\n2. bawang merah goreng\n3. kucai, iris'),
                                                height=70,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. Rebus air sampai mendidih. Masukkan jahe, kunyit bakar, dan daging. Masak sampai daging empuk. Angkat daging, saring kaldunya. Sisihkan.\n2. Rebus jeroan sapi di panci lain, masak sampai empuk. Buang air rebusan, tiriskan jeroan.\n3. Masukkan kembali daging ke dalam panci berisi kaldu sapi, tambahkan jeroan. Masak dengan api kecil.\n4. Tumis bumbu halus sampai wangi. Tambahkan daun salam, serai, lengkuas, cengkih, kayu manis, dan kapulaga. Aduk sampai matang. Angkat. Tuang ke dalam rebusan daging.\n5. Masukkan santan, garam, gula, dan kaldu sapi bubuk ke dalam rebusan daging. Masak sampai bumbu meresap. Angkat daging dan jeroan, tiriskan.\n6. Potong daging dan jeroan. Sesaat sebelum menyajikannya, masukkan dulu ke dalam panci berisi kuah panas. Tata dalam mangkuk saji, siram kuah. Taburi kucai, cabai bubuk, dan bawang goreng. Sajikan.'),
                                                height=450,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        elif page.route == "/gado-gado":
            page.views.append(
                ft.View(
                    route="/gado-gado",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/gado-gado.jpg',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Gado gado', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 2 buah tempe goreng\n2. 2 buah tahu goreng\n3. 2 buah telur rebus, kupas\n4. 1 buah kentang rebus, kupas kulitnya\n5. 4 lembar daun selada cina, cuci bersih\n6. 1/4 buah mentimun kupas, cuci bersih\n7. 1/2 buah wortel, bupas, iris\n8. 3 lonjor kacang panjang, iris 3 cm\n9. 50 gram toge, bersihkan akarnya\n10. 2 buah lontong'),
                                                height=210,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan untuk saus kacang:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 150 gram kacang tanah goreng\n2. 4 siung bawang putih, goreng\n3. 2 buah cabai merah, buang bijinya\n4. 1 1/2 (satu setengah) sdm gula merah, sisir\n5. 500 ml santan dari 1/4 butir kelapa\n6. 1 sdm air asam'),
                                                height=120,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan pelengkap:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. emping\n2. kerupuk udang\n3. bawang merah goreng\n4. kecap manis\n5. sambal cabai rawit'),
                                                height=100,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. siapkan blender. masukan kacang, bawang, cabai, gula merah, dan garam hingga halus\n2. rebus campuran kacang dengan santan\n3. Masak sambil aduk-aduk hingga matang dan meletup-letup. Angkat dan dinginkan.\n4. Rebus wortel, kacang panjang, dan taoge hingga matang. Angkat dan tiriskan.\n5. Potong semua bahan, termasuk lontong.\n6. Tata potongan lontong, tempe, tahu, kentang, telur, dan semua sayuran di piring saji.\n7. Siram dengan saus kacang.\n8. Sajikan gado-gado dengan pelengkapnya, seperti emping, kerupuk udang, bawang merah goreng, kecap manis, dan sambal.'),
                                                height=350,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        elif page.route == "/gudeg":
            page.views.append(
                ft.View(
                    route="/gudeg",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/gudeg.jpg',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Gudeg', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 1 kg nangka muda\n2. 5 butir telur ayam rebus, kupas\n3. 2 lembar daun salam\n4. 3 cm lengkuas, memarkan\n5. 120 gram gula jawa yang coklat tua\n6. 1.5 liter santan sedang\n7. 500 ml santan kental'),
                                                height=150,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bumbu:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 8 butir bawang merah\n2. 5 siung bawang putih\n3. 5 butir kemiri\n4. 1 sdm ketumbar\n5. 1 potong terasi\n6. 1/4 sdt jintan\n7. 2 sdt garam'),
                                                height=140,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan pelengkap:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. sambal goreng krecek\n2. opor ayam\n3. sambal bajak'),
                                                height=70,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. Potong nangka muda berbentuk dadu besar. Rebus nangka muda dalam air atau air kelapa tua secukupnya hingga lunak. Angkat dan tiriskan nangka muda.\n2. Bumbu Halus: Haluskan semua bahan bumbu dengan blender atau ulekan hingga halus benar.\n3. Masukkan nangka muda dan telur ke dalam panci. Tuangi santan, masukkan bumbu halus, daun salam, daun jeruk, lengkuas dan gula merah.\n4. Masak dengan api sedang hingga bumbu meresap dan kuahnya susut.\n5. Tuangkan santan kental. Masak dengan api hingga kuah benar-benar susut. Matikan api.\n6. Sajikan gudeg dengan pelengkapnya.'),
                                                height=350,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        elif page.route == "/karedok":
            page.views.append(
                ft.View(
                    route="/karedok",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/karedok.jpg',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Karedok', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 2 buah timun putih\n2. 5 buah terong hijau\n3. 5 helai kacang panjang\n4. 3 lembar daun kol\n5. 100 gram tauge, bersihkan\n6. 1 ikat daun kemangi\n7. 2 sdm air asam jawa\n8. 100 ml air matang'),
                                                height=170,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bumbu halus:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 100 gram kacang tanah goreng, giling halus\n2. 2 buah cabe merah keriting\n3. 2 buah cabe rawit merah\n4. 2 siung bawang putih\n5. 3 cm kencur\n6. 10 gram gula merah\n7. 1 sdt garam'),
                                                height=140,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan pelengkap:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. tepung kanji/emping'),
                                                height=30,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. Potong-potong timun ukuran kecil. Buang tangkai terong dan potong-potong tipis.\n2. Potong melintang kacang panjang dan daun kol 1 cm dan petiki daun kemangi.\n3. Siapkan air matang dalam wadah, beri sedikit garam. Rendam sayuran sebentar di dalamnya lalu angkat dan tiriskan hingga kering.\n4. Aduk Bumbu Halus dengan air asam dan air secukupnya hingga cukup kentalnya.\n5. Masukkan sayuran segar yang sudah dipotong dan tauge, aduk hingga terbalur rata dengan bumbu.\n6. Sajikan dengan topping kerupuk, jika suka.'),
                                                height=330,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        elif page.route == "/kolak":
            page.views.append(
                ft.View(
                    route="/kolak",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/kolak.jpg',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Kolak', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan bahan:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 2 buah pisang tanduk yang cukup tua, potong-potong\n2. 1 buah ubi jalar, potong kotak-kotak\n3. 500 ml santan encer\n4. 400 ml santan kental\n5. 200 gram gula merah sisir\n6. 1 sdm gula pasir\n7. 200 gram nangka, potong dadu kecil\n8. 2 lembar daun pandan, simpulkan\n9. Sedikit garam'),
                                                height=180,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. Rebus santan cair dengan gula merah, gula pasir, daun pandan ikat, dan garam. Aduk-aduk sampai gula merah mencair dan mengental.\n2. Masukkan potongan ubi jalar dan masak hingga ubi setengah empuk. Tambahkan pisang dan nangka, didihkan kembali.\n3. Masukkan santan kental, masak kolak ubi hingga mendidih sambil sesekali diaduk-aduk.\n4. Kalau sudah mendidih, angkat kolak ubi dan tuang ke piring saji. Sajikan selagi masih hangat.'),
                                                height=350,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        elif page.route == "/ketoprak":
            page.views.append(
                ft.View(
                    route="/ketoprak",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/ketoprak.jpg',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Ketoprak', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan bahan:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 150 gram taoge, seduh\n2. 200 gram bihun, seduh sampai lunak\n3. 5 buah lontong, potong\n4. 1 buah tahu putih\n5. 150 ml air 2 siung bawang putih, haluskan\n6. 1/2 sdt garam\n7. Minyak goreng secukupnya'),
                                                height=150,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bumbu kacang:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 200 gram kacang tanah kulit, goreng\n2. 200 ml air\n3. 1 1/2 sdt asam jawa dan 2 sdm air\n4. 2 buah cabai rawit merah\n5. 1 sdm gula merah, sisir halus'),
                                                height=100,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bumbu pelengkap:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 100 gram kerupuk kanji, goreng\n2. 3 sdm kecap manis\n3. 4 sdt bawang merah goreng untuk taburan'),
                                                height=70,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. Masukkan tahu ke mangkuk. Campur air, garam, dan bawang putih. Tuang ke mangkuk tahu. Diamkan sebentar. Angkat dan tiriskan. Goreng sampai kecoklatan. Potong dadu.\n2. Sambal kacang: campur kacang tanah, cabai rawit merah, bawang putih, gula merah, dan garam. Haluskan pakai ulekan atau blender.\n3. Campur asam jawa dan air, ambil 1/2 sendok makan air asam. Campur dengan bumbu kacang. Aduk rata.\n4. Tata lontong, bihun, taoge, dan tahu di dalam mangkuk. Siram sambal kacang. Tambahkan kecap manis sesuai selera. Taburi dengan bawang merah goreng dan kerupuk kanji.'),
                                                height=320,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        elif page.route == "/martabak":
            page.views.append(
                ft.View(
                    route="/martabak",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/martabak.jpg',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Martabak', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan kulit:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 200 gram tepung terigu protein tinggi\n2. 1/4 sendok teh garam\n3. 140 ml air 30 gram minyak goreng\n4. 500 ml minyak goreng untuk merendam\n5. 500 ml minyak untuk menggoreng'),
                                                height=100,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bumbu isian:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 500 gram daging giling\n2. 100 gram ayam giling\n3. 3 siung bawang putih, iris tipis\n4. 6 butir bawang merah, iris tipis\n5. 2 buah cabai merah, cincang halus\n6. 2 sendok teh kari bubuk7. 1 sendok teh garam\n8. 1/4 sendok teh merica bubuk\n9. 1/2 sendok teh gula pasir\n10. 1 batang daun bawang, diiris halus\n11. 1 sendok makan minyak untuk menumis'),
                                                height=210,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bumbu campuran:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 25 gram daun bawang, iris halus\n2. 1 butir telur bebek, kocok lepas\n3. 1 butir telur ayam, kocok lepas\n4. 1/2 buah (50 gram) bawang bombay, cicang halus\n5. 1/4 sendok teh garam\n6. 1/8 sendok teh merica bubuk\n7. 50 gram bahan tumisan daging'),
                                                height=150,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. Buat kulit martabak terlebih dahulu, campur tepung terigu dan garam. Tuang air sedikit demi sedikit sambil diuleni sampai kalis. Tambahkan minyak goreng. Uleni sampai elastis.\n2. Timbang masing-masing 75 gram. Bulatkan. rendam dalam minyak goreng selama dua jam.\n3. Buat isian martabak, tumis bawang putih, bawang merah, dan cabai merah sampai harum. Tambahkan daging giling dan ayam giling. Aduk sampai berubah warna.\n4. Masukkan kari bubuk, garam, merica bubuk, dan gula pasir. Aduk sampai meresap. Tambahkan daun bawang. Aduk rata. Sisihkan.\n5. pipihkan kulit dan giling tipis, sisihkan\n6. Panaskan minyak dalam teflon. Letakkan selembar kulit. Beri campuran isi. Lipat. Goreng dengan sedikit minyak (jangan sampai terendam) sambil disiram-siram minyak sampai matang.'),
                                                height=400,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        elif page.route == "/mie-aceh":
            page.views.append(
                ft.View(
                    route="/mie-aceh",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/mie-aceh.jpg',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Mie aceh', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 400 gram mi kuning basah, siap pakai\n2. 150 gram daging sapi has dalam, iris dadu kecil\n3. 150 gram udang, belah menjadi 2 bagian\n4. 100 gram taoge\n5. 100 gram kol\n6. 1 L air\n7. 3 sdm daun bawang iris\n8. 2 sdm seledri iris\n9. 3 sdm minyak goreng'),
                                                height=180,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bumbu halus:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 4 sdm bawang merah iris\n2. 3 sdm bawang putih iris\n3. 3 sdm cabai merah\n4. 1 sdm kunyit iris\n5. 1 sdt jintan\n6. 1 sdt merica\n7. 1 sdm garam'),
                                                height=140,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. Nyalakan api sedang kompor, panaskan tiga sendok makan minyak. Tumis bumbu halus yang sudah dihaluskan hingga harum.\n2. Di panci lain, rebus udang dan daging sapi dengan 1 liter air. Tutup panci selama 10 menit agar daging empuk. Kalau sudah empuk, angkat dan tiriskan.\n3. Masukkan kol ke dalam tumisan, tumis hingga layu. Masukkan mi kuning basah, daun bawang, cuka, dan seledri. Aduk hingga bumbu merata. Tambahkan daging dan udang. Aduk kembali.\n4. Matikan api kompor dan angkat. Hidangkan mi aceh goreng saat panas, taburi dengan bawang goreng, daun seledri iris, acar mentimun, dan emping goreng.'),
                                                height=360,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        elif page.route == "/nasi-kuning":
            page.views.append(
                ft.View(
                    route="/nasi-kuning",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/nasi-kuning.jpg',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Nasi kuning', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan bahan:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 1 kg beras\n2. 3 batang serai, memarkan\n3. 10 lembar daun salam\n4. 2 ruas lengkuas, memarkan\n5. 8 ruas kunyit\n6. 10 siung bawang merah, haluskan\n7. 1 liter santan\n8. 1 sdm garam\n9. air secukupnya'),
                                                height=180,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. Haluskan kunyit bersama santan menggunakan blender, lalu saring.\n2. Rebus campuran santan dan kunyit bersama serai, daun salam, lengkuas, garam, dan bawang merah yang telah dihaluskan hingga mendidih dengan api sedang.\n3. Masukkan beras, lalu aduk hingga tercampur rata. Masak beras hingga setengah matang. Tambahkan sedikit air jika nasi setengah matang tampak terlalu kering\n4. Pindahkan nasi kuning setengah matang ke dalam panci kukusan. Kemudian, kukus nasi kuning hingga matang.'),
                                                height=300,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        elif page.route == "/nasi-goreng":
            page.views.append(
                ft.View(
                    route="/nasi-goreng",
                    padding=20,
                    spacing=0,
                    controls=[
                        AppBar,
                        ft.ListView(
                            expand=True,
                            controls=[
                                ft.Column(
                                    spacing=10,
                                    controls=[
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.CENTER,
                                            controls=[
                                                ft.Stack(
                                                    controls=[
                                                        ft.Container(
                                                            height=220,
                                                            width=200,
                                                            image_src='makanan/nasi-goreng.jpg',
                                                            image_fit=ft.ImageFit.COVER,
                                                            border_radius=10,
                                                            alignment=ft.alignment.bottom_center
                                                        ),
                                                        ft.Container(
                                                            height=250,
                                                            width=200,
                                                            # bgcolor=ft.colors.BLUE,
                                                            border_radius=10,
                                                            content=ft.Text('Nasi goreng', weight=ft.FontWeight.BOLD, size=20),
                                                            alignment=ft.alignment.bottom_center
                                                        )
                                                    ]
                                                )
                                            ]
                                        ),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 500 gr nasi\n2. 3 sdm minyak sayur\n3. 150 gr daging ayam goreng suwir\n4. 3 sdm kecap manis\n5. 2 butir telur ayam\n6. 1 sdm kaldu bubuk non MSG\n7. 1/2 sdt merica bubuk'),
                                                height=140,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bumbu halus:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. 5 butir bawang merah\n2. 3 siung bawang putih\n3. 3 buah cabe merah\n4. 2 sdt terasi goreng\n5. 2 sdt garam'),
                                                height=100,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Bahan pelengkap:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. kerupuk kanji\n2. acar mentimun'),
                                                height=40,
                                                width=380
                                            )
                                        ]),
                                        ft.Row(
                                            alignment=ft.MainAxisAlignment.START,
                                            controls=[
                                                ft.Container(
                                                    
                                                    content=ft.Text('Cara membuat:', weight=ft.FontWeight.BOLD)
                                                )
                                            ]
                                        ),
                                        ft.Row(alignment=ft.MainAxisAlignment.START, controls=[
                                            ft.Container(
                                                content=ft.Text('1. Panaskan minyak, tumis bumbu halus hingga wangi.\n2. Kocok telur hingga rata. Tuangkan ke dalam bumbu. Aduk rata.\n3. Masukkan nasi, ayam suwir, kaldu bubuk, kecap manis dan merica.\n4. Aduk-aduk hingga seluruhnya tercampur rata dan agak kering.\n5. Angkat dan sajikan dengan Pelengkapnya.'),
                                                height=250,
                                                width=380
                                            )
                                        ])
                                    ]
                                )
                            ]
                        )
                    ]
                )
            ),
        page.update()

    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    page.on_route_change = route_change
    page.on_view_pop = view_pop
    page.go(page.route)

ft.app(target=main, view=ft.AppView.WEB_BROWSER, assets_dir='assets')