def tower(n,source,target,additional):
   if n == 1:
      print(f"Move disk 1 from {source} to {target}")
   else:
      tower(n-1,source,additional,target)
      print(f"Move disk {n} from {source} to {target}")
      tower(n-1,additional,target,source)
tower(3,'A','C',"B")