class Persona(object):
    """
    """
    
    def __init__(self, n, n1, n2, n3):
        """
        """
        self.Alumno = n
        self.nota1 = float(n1)
        self.nota2 = float(n2)
        self.nota3 = float(n3)

    def agregar_Alumno(self, n):
        """
        """
        self.Alumno = n

    def obtener_Alumno(self):
        """
        """
        return self.Alumno

    def agregar_nota1(self, n1):
        """
        """
        self.nota1 = float(n1)

    def obtener_nota1(self):
        """
        """
        return self.nota1
    
    def agregar_nota2(self, n2):
        """
        """
        self.nota2 = float(n2)

    def obtener_nota2(self):
        """
        """
        return self.nota2
    
    def agregar_nota3(self, n3):
        """
        """
        self.nota3 = float(n3)

    def obtener_nota3(self):
        """
        """
        return self.nota3
    def calcular_promedio(self):
        """
        """
        promedio = ((self.obtener_nota1()+self.obtener_nota2()+self.obtener_nota3())/3)
        return promedio
    def __str__(self):
        """
        """
        return "EL nombre del alumno: %s con un promedio de: -%d\n   " % (self.Alumno, self.promedio )