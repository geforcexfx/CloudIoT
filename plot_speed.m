close all
clear
mid = 156.7+[327.7 362.7 416.7' 587 898.7 1616.7]';
mid0 = [327.7 362.7 416.7 587 898.7 1616.7]';
high = 462+ [381.3 465 616.7 1163 1883.3 3583.3]';
high0 = [381.3 465 616.7 1163 1883.3 3583.3]';
low = 45+[300.3 317.7 311.3 369.3 450 629.7]';
low0 = [300.3 317.7 311.3 369.3 450 629.7]';
pi = [468 1059 3167];

res = [76800 307200 768432];

speed = [50 10 5 2 1 0.5];
send = [326 328 326 351 542.7 1656 2787 13091 24988]; 

n320 = sp(22,speed)*1000;
n640 = sp(60,speed)*1000;
n1024 = sp(173,speed)*1000;

figure('units','normalized','outerposition',[0 0 1 1],'Name','1')
    %ylim([0, max(counts) * 1.2]);
    bar(speed,mid,'FaceColor','c')
    hold on
    
    bar(speed,mid0,'FaceColor','g');
    hold on
    
    b8 = plot(speed,mid);
    hold on
    b9 = plot(speed,n640,'b--o');
    ylabel('Time to send an image (ms)')
    xlabel('Network bandwidth (Mbps)')
    title('Bottleneck of the network speed with 640x480(60Kb) image')
    legend([b8 b9] , {'latency in practice','latency in theory'})
    xticks([0.5 1 2 5 10 50])
    ylim([0, max(mid) * 1.1])
    xlim([0,51])
    for i = 1:numel(speed)
        
        if i == 1
            text(speed(1) - 1, mid(1) + 80, num2str(mid(1)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        else
            text(speed(i) - 0.2, mid(i) + 80, num2str(mid(i)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        end   
    end 
    
      for i = 1:numel(speed)
        
        if i == 1
            text(speed(1) - 2, mid0(1) + 80, num2str(mid0(1)), 'Color','blue','VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        else
            text(speed(i) + 0.5, mid0(i) + 80, num2str(mid0(i)),'Color','blue', 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        end   
      end 
    for i = 1:numel(speed)
%         
        if i == 5 || i == 6
            text(speed(i) -0.5 , n640(i) , num2str(n640(i)), 'Color','magenta','VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        elseif i ==1 
             text(speed(1) - 1, n640(1), num2str(n640(1)), 'Color','magenta','VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        else  
            text(speed(i) + 0.5 , n640(i) , num2str(n640(i)),'Color','magenta', 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        end   
    end 
    %saveas(gcf,'net_640.png')    
figure('units','normalized','outerposition',[0 0 1 1],'Name','2')
    %ylim([0, max(counts) * 1.2]);
    bar(speed,high,'FaceColor','c')
    hold on
    
    bar(speed,high0,'FaceColor','g');
    hold on
    
    b8 = plot(speed,high);
    hold on
    b9 = plot(speed,n1024,'b--o');
    ylabel('Time to send an image (ms)')
    xlabel('Network bandwidth (Mbps)')
    title('Bottleneck of the network speed with 1024x768(175Kb) resolution image')
    legend([b8 b9] , {'latency in practice','latency in theory'})
    xticks([0.5 1 2 5 10 50])
    ylim([0, max(high) * 1.1])
    xlim([0,51])
    for i = 1:numel(speed)
        
        if i == 1
            text(speed(1) - 1, high(1) + 100, num2str(high(1)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        else
            text(speed(i) - 0.2, high(i) + 100, num2str(high(i)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        end   
    end 
    
      for i = 1:numel(speed)
        
        if i == 1
            text(speed(1) - 2, high0(1) + 80, num2str(high0(1)), 'Color','blue','VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        else
            text(speed(i) + 0.5, high0(i) + 80, num2str(high0(i)),'Color','blue', 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        end   
      end 
    for i = 1:numel(speed)
%         
        if i == 5 || i == 6
            text(speed(i) -0.5 , n1024(i)+150 , num2str(n1024(i)), 'Color','magenta','VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        elseif i ==1 
             text(speed(1) - 2, n1024(1), num2str(n1024(1)), 'Color','magenta','VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        else
            text(speed(i) + 0.5 , n1024(i) , num2str(n1024(i)),'Color','magenta', 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        end   
    end 
    %saveas(gcf,'net_1024.png')
figure('units','normalized','outerposition',[0 0 1 1],'Name','3')
    %ylim([0, max(counts) * 1.2]);
    bar(speed,low,'FaceColor','c')
    hold on
    
    bar(speed,low0,'FaceColor','g');
    hold on
    
    b8 = plot(speed,low);
    hold on
    b9 = plot(speed,n320,'b--o');
    ylabel('Time to send an image (ms)')
    xlabel('Network bandwidth (Mbps)')
    title('Bottleneck of the network speed with 320x240(22Kb) resolution image')
    legend([b8 b9] , {'latency in practice','latency in theory'})
    xticks([0.5 1 2 5 10 50])
    ylim([0, max(low) * 1.1])
    xlim([0,51])
    for i = 1:numel(speed)
        
        if i == 1
            text(speed(1) - 1, low(1) + 15, num2str(low(1)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        else
            text(speed(i) - 0.2, low(i) + 15, num2str(low(i)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        end   
    end 
    
      for i = 1:numel(speed)
        
        if i == 1
            text(speed(1) - 2, low0(1) + 8, num2str(low0(1)), 'Color','blue','VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        else
            text(speed(i) + 0.5, low0(i) + 8, num2str(low0(i)),'Color','blue', 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        end   
      end 
    for i = 1:numel(speed)
%         
        if i == 5 || i == 6
            text(speed(i) -0.5 , n320(i)+20 , num2str(n320(i)), 'Color','magenta','VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        elseif i ==1 
             text(speed(1) - 2, n320(1), num2str(n320(1)), 'Color','magenta','VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        else
            text(speed(i) + 0.5 , n320(i) , num2str(n320(i)),'Color','magenta', 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        end   
    end 
    %saveas(gcf,'net_320.png')
figure (4)
    bar(76800,pi(1),80000, 'FaceColor','g')
    hold on
    bar(307200,pi(2),80000, 'FaceColor','y')
    hold on
    bar(786432,pi(3),80000, 'FaceColor','m')
    hold on
    plot(res,pi)
    ylabel('Time to process an image (ms)')
    xlabel('Image resolution')
    title('Image process on Raspberry pi')
    xticks([76800 307200 786432])
    legend('320x240', '640x480', '1024x768', 'location', 'northwest')
    ylim([0, max(pi) * 1.1])
    xlim([20000,870433])
     
    for i = 1:numel(res)
        
        if i == 1
            text(res(1) - 3, pi(1) + 40, num2str(pi(1)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        else
            text(res(i)-20 , pi(i) + 120, num2str(pi(i)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        end   
    end
    %saveas(gcf,'pi_pro.png')
    
figure('units','normalized','outerposition',[0 0 1 1],'Name','5')
    bar(speed,mid, 'FaceColor','b')
    hold on
    b1 = plot(speed,mid);
    hold on
    b2 = plot(linspace(0,60,2) ,[1059 1059]);

    ylabel('Time to send an image (ms)')
    xlabel('Network bandwidth (Mbps)')
    title('Comparision of process speed between cloud server and pi with 640x480 resolution image')
    legend([b1 b2], {'server process', 'pi process'})
    ylim([0, max(mid) * 1.1])
    xlim([0,51])
    xticks([0.5 1 2 5 10 50])
    text(29 , pi(2) + 90, num2str(pi(2)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
    for i = 1:numel(speed)
        
        if i == 1
            text(speed(1) - 3, mid(1) + 80, num2str(mid(1)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        else
            text(speed(i) - 0.2, mid(i) + 80, num2str(mid(i)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        end   
    end 
    %print('-bestfit',['fit_model','640'],'-dpdf')
     %saveas(gcf,'compare_640.png')
figure('units','normalized','outerposition',[0 0 1 1],'Name','6')
    bar(speed,high, 'FaceColor','b')
    hold on
    b1 = plot(speed,high);
    hold on
    b2 = plot(linspace(0,60,2) ,[3167 3167]);

    ylabel('Time to send an image (ms)')
    xlabel('Network bandwidth (Mbps)')
    title('Comparision of process speed between cloud server and pi with 1024x768 resolution image')
    legend([b1 b2], {'server process', 'pi process'})
    ylim([0, max(high) * 1.1])
    xlim([0,51])
    xticks([0.5 1 2 5 10 50])
    text(29 , pi(3) + 90, num2str(pi(3)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
    for i = 1:numel(speed)
        
        if i == 1
            text(speed(1) - 1, high(1) + 150, num2str(high(1)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        else
            text(speed(i) - 0.2, high(i) + 150, num2str(high(i)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        end   
    end 
    %saveas(gcf,'compare_1024.png')
%     %print('-bestfit',['fit_model','1024'],'-dpdf')
%  figure(7)
figure('units','normalized','outerposition',[0 0 1 1],'Name','7')
    bar(speed,low, 'FaceColor','b')
    hold on
    b1 = plot(speed,low);
    hold on
    b2 = plot(linspace(0,60,2) ,[468 468]);

    ylabel('Time to send an image (ms)')
    xlabel('Network bandwidth (Mbps)')
    title('Comparision of process speed between cloud server and pi with 320x240 resolution image')
    legend([b1 b2], {'server process', 'pi process'})
    ylim([0, max(low) * 1.1])
    xlim([0,51])
    xticks([0.5 1 2 5 10 50])
    text(29 , pi(1) + 20, num2str(pi(1)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
    for i = 1:numel(speed)
        
        if i == 1
            text(speed(1) - 1.5, low(1) + 20, num2str(low(1)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        else
            text(speed(i) - 0.2, low(i) + 20, num2str(low(i)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
        end   
    end 
%     %print('-bestfit',['fit_model','320'],'-dpdf')
 %saveas(gcf,'compare_320.png')
byte = [1 3 4 5 6 7 8 9 10];    
figure('units','normalized','outerposition',[0 0 1 1],'Name','8')
    bar(1, send(1),'FaceColor','k')
    hold on
    bar(3, send(2) ,'FaceColor','b')
    hold on
    bar(4, send(3), 'FaceColor','r')
    hold on
    bar(5, send(4), 'FaceColor','g')
    hold on
    bar(6, send(5), 'FaceColor','w')
    hold on
    bar(7, send(6), 'FaceColor','c')
    hold on
    bar(8, send(7), 'FaceColor','m')
    hold on
    bar(9, send(8), 'FaceColor','y')
    hold on
    bar(10, send(9), 'FaceColor','none', 'LineStyle', '--')
    plot(byte, send)
    ylabel('Time to send an image (ms)')
    xlabel('File size(byte)')
    title('Measurement of the time it takes to send files with different size')
    legend('1 byte', '1Kb', '10Kb', '100Kb', '1 Mb', '5Mb', '10Mb', '50Mb', '100Mb', 'location', 'northwest')
     ylim([0, max(send) * 1.1])
    xlim([0.5,11])
    
    for i = 1:numel(send)
        
        text(byte(i) - 0.2, send(i) + 1000, num2str(send(i)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
     
    end 
    %print('-bestfit',['fit_model','320'],'-dpdf')
    %saveas(gcf,'size_total.png')
pi2 = [468,45
       1059,156.7 
       3167,467];
   serve = [45 156.7 467]
figure(9)
    bar(res, pi2)

    ylabel('Time to process an image (ms)')
    xlabel('resolution(pixels)')
    title('Comparision of the time it takes to process an image in different resolutions')
    legend('Pi', 'cloud server', 'location', 'northwest')
     ylim([0, max(pi) * 1.1])
    %xlim([0.5,11])
    
    for i = 1:3
        
        text(res(i) - 50000, pi(i) + 150, num2str(pi(i)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
     
    end
    for i = 1:3
        
        text(res(i) - 900, serve(i) + 170, num2str(serve(i)), 'VerticalAlignment', 'top', 'FontSize', 10, 'FontWeight', 'bold')
     
    end 
%     %print('-bestfit',['fit_model','320'],'-dpdf')
     saveas(gcf,'compare_picloud.png')
 function f = sp(n,m)
    f = (n*10^3*8)./(m*10^6);
    end