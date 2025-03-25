permutaciones :: [a] -> [[a]]
permutaciones lista = undefined

conseguirTodasPermutacionesHastaN :: Int -> [[Int]]
conseguirTodasPermutacionesHastaN a = undefined


noRepetidos :: [Int] -> Bool
noRepetidos [] = True
noRepetidos (x:xs) | noRepetidosValor x xs = noRepetidos xs
                   | otherwise = False

noRepetidosValor :: Int -> [Int] -> Bool
noRepetidosValor _ [] = True
noRepetidosValor valor (x:xs) 
    | valor == x = False
    | otherwise = noRepetidosValor valor xs
{-
    Voy a intentar conseguir uno que tenga todas las permutaciones posibles

-}

--valores :: [Int] -> [[Int]]
--valores [] = []
--valores y = x : (eliminarNElemento x y)  [ x <-[0..(length y) - 1]]--

eliminarNElemento :: Int -> [Int] -> [Int]
eliminarNElemento _ [] = []
eliminarNElemento 0 (x:xs) = xs
eliminarNElemento x (y:ys) = y : eliminarNElemento (x - 1) ys

sumasParciales :: Num a => [a] -> [a]
sumasParciales xs = reverse  $ foldr (\x acc-> if null acc 
                                 then x : acc 
                                else (x + (head acc)) : acc) [] (reverse xs)

--sumaAlt :: Num a => [a] -> [a]
--sumaAlt lista = sumasParciales (negativosDeImpares lista)

sumaAltInverso lista = reverse $ sumasParciales $ reverse (foldr (\x acc -> if even (length acc)
                                 then x : acc
                                 else -x : acc) [] lista)

sumaAlt lista = sumasParciales $ if even (length lista)
                                                   then zipWith (*) listaInvertida [-1, -1..]
                                                   else listaInvertida
    where listaInvertida = (foldr (\x acc -> if even (length acc)
                            then x : acc
                            else -x : acc) [] lista)



negativosDeImpares :: Num a => [a] -> [a]
negativosDeImpares [] = [] 
negativosDeImpares (x:xs) = (x) : positivosDeImpares  xs

positivosDeImpares :: Num a => [a] -> [a]
positivosDeImpares [] = []
positivosDeImpares (x:xs) = -x : negativosDeImpares xs 


-- Hago el negatvio de los impares y lo consegui ya

partes :: [Int] -> [Int]
partes [] = []
partes (x:xs) = x : xs
