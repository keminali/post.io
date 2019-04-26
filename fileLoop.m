n=1000;
fileinfo = importdata('transient.case',';');
for i=1:n
filename=sprintf('transient_%d.case',i);
a=cell2mat(fileinfo(13));
idx=find(a==':');
fileinfo(13)=cellstr(strrep(a,a(idx+2:end),num2str(i)));
filePh = fopen(filename,'w');
fprintf(filePh,'%s\n',fileinfo{:});
fclose(filePh);
end

