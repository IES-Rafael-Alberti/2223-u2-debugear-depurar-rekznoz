from src.burbuja import algoritmo_burbuja

def test_algoritmo_burbujag():
        assert algoritmo_burbuja([4, 2, 1, 3]) == [1, 2, 3, 4]
        assert algoritmo_burbuja([4.2, 2.1, 1.3, 3.7]) == [1.3, 2.1, 3.7, 4.2]
        assert algoritmo_burbuja([]) == []
        assert algoritmo_burbuja([1]) == [1]