for a=0:9
    for b=0:9
        for c=0:9
            for d=0:9
                for e=0:9
                    if a~=b && a~=c && a~=d && a~=e && b~=c && b~=d &&  b~=e &&  c~=d &&  c~=e &&  d~=e
                        m1 = a * 1000 + b * 100 + c * 10 + d;
                        m2 = a * 1000 + b * 100 + e * 10 + d;
                        s = e * 10000 + d * 1000 + c * 100 + a * 10 + d;
                        if s==m1+m2
                            disp(a)
                            disp(b)
                            disp(c)
                            disp(d)
                            disp(e)
                        end
                    end
                end
            end
        end
    end
end
                        