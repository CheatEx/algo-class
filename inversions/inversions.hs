module Main (main, inversions,
             sortAndCount, mergeAndCount)
where

import System.IO
import Data.List

inversions :: (Ord a) => [a] -> Integer
inversions = snd . sortAndCount

sortAndCount :: (Ord a) => [a] -> ([a], Integer)
sortAndCount []  = ([], 0)
sortAndCount [e] = ([e], 0)
sortAndCount a   =
  let splitPos = div (length a) 2
      (h1, h2) = splitAt splitPos a
      (b, x) = sortAndCount h1
      (c, y) = sortAndCount h2
      (d, z) = mergeAndCount b c
  in 	(d, x + y + z)

mergeAndCount :: (Ord a) => [a] -> [a] -> ([a], Integer)
mergeAndCount b        []       = (b, 0)
mergeAndCount []       c        = (c, 0)
mergeAndCount b@(x:xs) c@(y:ys) =
  if (x < y)
    then let (list, cnt) = mergeAndCount xs c
         in (x:list, cnt)
    else let (list, cnt) = mergeAndCount b  ys
         in (y:list, cnt + (genericLength b))

main = do
    h <- openFile "IntegerArray.txt" ReadMode
    c <- hGetContents h
    let l = map (read::String->Integer) $ lines c
    putStrLn $ show $ inversions l
