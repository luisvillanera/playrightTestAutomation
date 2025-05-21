class LoginPageLocators:
    """
    Locators para la página de login https://practicetestautomation.com/practice-test-login/
    
    Tipos de selectores disponibles:
    1. ID (#)              -> Ejemplo: #username
    2. Clase (.)           -> Ejemplo: .error-message
    3. Tag                 -> Ejemplo: button
    4. Atributo []        -> Ejemplo: [data-test="login"]
    5. Texto              -> Ejemplo: text="Login"
    6. XPath              -> Ejemplo: //button[@type='submit']
    7. CSS Combinado      -> Ejemplo: form#login input[type="text"]
    8. nth-child          -> Ejemplo: li:nth-child(2)
    """
    
    # ====== LOCATORS ACTUALES EN USO ======
    
    # Campo de usuario - usando ID
    USERNAME_INPUT = "#username"
    
    # Campo de contraseña - usando ID
    PASSWORD_INPUT = "#password"
    
    # Botón de submit - usando ID
    SUBMIT_BUTTON = "#submit"
    
    # Mensaje de éxito - usando clase CSS
    SUCCESS_MESSAGE = ".has-text-align-center"
    
    # Mensaje de error - usando ID
    ERROR_MESSAGE = "#error"
    
    # ====== EJEMPLOS DE OTROS TIPOS DE SELECTORES ======
    
    # === Selectores por ID ===
    # ID_SELECTOR = "#login-form"              # Selecciona elemento con id="login-form"
    # ID_WITH_SPECIAL = "#login-form-123"      # IDs pueden contener números y guiones
    
    # === Selectores por Clase ===
    # CLASS_SELECTOR = ".error-message"        # Selecciona elementos con class="error-message"
    # MULTIPLE_CLASSES = ".btn.btn-primary"    # Selecciona elementos con ambas clases
    
    # === Selectores por Tag ===
    # TAG_SELECTOR = "button"                  # Selecciona todos los elementos <button>
    # INPUT_TAG = "input"                      # Selecciona todos los elementos <input>
    
    # === Selectores por Atributo ===
    # ATTR_EQUALS = "[type='submit']"          # Atributo exacto
    # ATTR_CONTAINS = "[class*='btn']"         # Atributo contiene
    # ATTR_STARTS = "[id^='login']"            # Atributo empieza con
    # ATTR_ENDS = "[id$='button']"             # Atributo termina con
    
    # === Selectores por Texto ===
    # TEXT_EXACT = "text='Login'"              # Texto exacto
    # TEXT_CONTAINS = "text=Log"               # Texto contiene
    # TEXT_REGEX = "text=/^Log/"               # Texto con regex
    
    # === Selectores XPath ===
    # XPATH_BASIC = "//button"                 # Todos los botones
    # XPATH_WITH_ID = "//button[@id='submit']" # Botón con ID específico
    # XPATH_CONTAINS = "//div[contains(@class, 'error')]"  # Contiene clase
    # XPATH_TEXT = "//button[text()='Login']"  # Texto exacto
    # XPATH_PARENT = "//input[@id='username']/parent::div"  # Elemento padre
    # XPATH_CHILD = "//form/child::input"      # Elemento hijo
    
    # === Selectores CSS Combinados ===
    # FORM_INPUT = "form input"                # Input dentro de form
    # FORM_SPECIFIC_INPUT = "form#login input[type='text']"  # Input específico
    # DIRECT_CHILD = "form > input"            # Hijo directo
    # SIBLING = "label + input"                # Elemento siguiente
    
    # === Selectores nth-child ===
    # FIRST_ITEM = "li:first-child"           # Primer elemento
    # LAST_ITEM = "li:last-child"             # Último elemento
    # SECOND_ITEM = "li:nth-child(2)"         # Segundo elemento
    # EVEN_ITEMS = "li:nth-child(even)"       # Elementos pares
    
    # === Selectores Compuestos ===
    # COMPLEX_1 = "#login-form input:not([type='hidden'])"  # Excluye inputs ocultos
    # COMPLEX_2 = ".form-group:has(input[type='text'])"     # Grupo que contiene input
    # COMPLEX_3 = "button:enabled"             # Botones habilitados
    # COMPLEX_4 = "input:required"             # Inputs requeridos
    
    # === Selectores para Estados ===
    # HOVER_STATE = "button:hover"             # Estado hover
    # ACTIVE_STATE = "button:active"           # Estado active
    # FOCUS_STATE = "input:focus"              # Estado focus
    # CHECKED_STATE = "input:checked"          # Estado checked
    
    # === Selectores Responsivos ===
    # MOBILE_MENU = "[data-mobile-menu]"       # Elementos específicos móvil
    # DESKTOP_ONLY = "[data-desktop-only]"     # Elementos solo desktop
    
    # === Selectores de Aria (Accesibilidad) ===
    # ARIA_LABEL = "[aria-label='Login']"      # Por aria-label
    # ARIA_ROLE = "[role='button']"            # Por rol
    # ARIA_EXPANDED = "[aria-expanded='true']"  # Por estado expandido 