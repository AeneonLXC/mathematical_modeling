clear clf 
%区域大小 
rec_x1=75; 
rec_x2=200; 
rec_y1=-50; 
rec_y2=150; 
%原始数据 
x=[129.0 140.0 103.5 88.0 185.5 195.0 105.5 157.5 107.5 77.0 81.0 162.0 162.0 117.5];
y=[7.5 141.5 23.0 147.0 22.5 137.5 85.5 -6.5 -81 3.0 56.5 -66.5 84.0 -33.5]; 
z=[4 8 6 8 6 8 8 9 9 8 8 9 4 9]; 
%插值 
[xx,yy]=meshgrid([rec_x1:4:rec_x2],[rec_y1:4:rec_y2]); 
zz=griddata(x,y,z,xx,yy,'cubic'); 
%做出区域水深图 
surf(xx,yy,zz); 
%做出危险区域图 
figure(2)
nz=find(zz<5); 
dan_x=xx(nz);
dan_y=yy(nz); 
dan_z=zz(nz); 
plot(dan_x,dan_y,'*') 
axis([rec_x1,rec_x2,rec_y1,rec_y2])