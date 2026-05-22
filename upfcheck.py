import usefulpyfunc as upf

upf.get_help()

upf.equal_not_strict(10, 10.0)
upf.equal_not_strict(10, 12.0)
upf.equal_strict(10, 10)
upf.equal_strict(10, 10.0)
upf.check_type(10)
upf.check_type(10.0)
upf.check_type("ten")
upf.check_type(False)

array1 = [10, 10.0, 12, 5.4, -5, 0]

upf.equal_not_strict_arr(array1, "array1", 1)
upf.equal_not_strict_arr(array1, "array1", 2)
upf.equal_strict_arr(array1, "array1", 1)
upf.equal_strict_arr(array1, "array1", 2)
upf.check_type_arr(array1, "array1")

array_wrong = ["hi", 10, 100, 100.0, -100.0, -100, 183, 0, 26, True]

upf.equal_not_strict_arr(array_wrong, "arr_wrong", 1)
upf.equal_not_strict_arr(array_wrong, "arr_wrong", 2)
upf.equal_strict_arr(array_wrong, "arr_wrong", 1)
upf.equal_strict_arr(array_wrong, "arr_wrong", 2)
upf.check_type_arr(array_wrong, "arr_wrong")

randarr_int = []
randarr_uni = []

upf.random_array_int(10, -100, 100, "RandomIntArray", randarr_int)
upf.random_array_uni(10, -100, 100, "RandomUniArray", randarr_uni)
upf.check_type_arr(randarr_int, "RandIntArr")
upf.check_type_arr(randarr_uni, "RandUniArr")

upf.random_rounded(10, 0, 20)