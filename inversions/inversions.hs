module Main (main, sortAndCount, mergeAndCount)
where

import System.IO
import Data.List

sortAndCount :: (Ord a) => [a] -> ([a], Integer)
sortAndCount []  = ([], 0)
sortAndCount [e] = ([e], 0)
sortAndCount l   =
  let ll =  length l
      splitPos = div ll 2
      (h1, h2) = splitAt splitPos l
      (b, x) = sortAndCount h1 
      (c, y) = sortAndCount h2
      (d, z) = mergeAndCount b c
  in 	(d, x + y + z)

mergeAndCount :: (Ord a) => [a] -> [a] -> ([a], Integer)
mergeAndCount b c =
  let (l, x) = mergeAndCountLoop b c ([], 0)
  in  (reverse l, x)

mergeAndCountLoop :: (Ord a) => [a] -> [a] -> ([a], Integer) -> ([a], Integer)
mergeAndCountLoop b       []      (acc, x) = ( (reverse b)++acc, x)
mergeAndCountLoop []      c       (acc, x) = ( (reverse c)++acc, x)
mergeAndCountLoop (bh:bt) (ch:ct) (acc, x) = 
  if bh < ch 
    then mergeAndCountLoop bt (ch:ct) (bh:acc, x)
    else mergeAndCountLoop (bh:bt) ct (ch:acc, x + (genericLength bt) + 1)

main = do
    h <- openFile "IntegerArray.txt" ReadMode
    c <- hGetContents h
    let l = map (read::String->Integer) $ lines c
    let (_, inv) = sortAndCount l
    putStrLn $ show inv