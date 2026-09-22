% train_knn.m — MFCC + KNN bird song classifier
clear; clc;

%% Config
trainDir = 'clips';          % contains subfolders, one per species
testSplit = 0.2;             % 20% held out for testing
numMFCC  = 13;
k        = 5;
fs       = 22000;

%% Collect files and labels
species = dir(trainDir);
species = species([species.isdir] & ~startsWith({species.name}, '.'));
X = []; Y = {};

for s = 1:numel(species)
    label = species(s).name;
    files = dir(fullfile(trainDir, label, '*.wav'));
    fprintf('Loading %s: %d files\n', label, numel(files));
    for f = 1:numel(files)
        fp = fullfile(trainDir, label, files(f).name);
        [x, fsIn] = audioread(fp);
        if fsIn ~= fs
            x = resample(x, fs, fsIn);
        end
        aFE = audioFeatureExtractor(SampleRate=fs, ...
            mfcc=true, mfccDelta=true, mfccDeltaDelta=true);
        setExtractorParameters(aFE, 'mfcc', 'NumCoeffs', numMFCC);
        feats = extract(aFE, x);            % frames x (3*numMFCC)
        X = [X; mean(feats), std(feats)];   % 1 x (6*numMFCC) per clip
        Y{end+1,1} = label; %#ok<SAGROW>
    end
end

fprintf('Feature matrix: %d clips x %d features\n', size(X,1), size(X,2));

%% Train/test split
cv = cvpartition(Y, 'HoldOut', testSplit);
idxTrain = training(cv);
idxTest  = test(cv);

%% Train KNN
mdl = fitcknn(X(idxTrain,:), Y(idxTrain), 'NumNeighbors', k, ...
              'Prior', 'uniform');

%% Evaluate
pred = predict(mdl, X(idxTest,:));
acc  = mean(strcmp(pred, Y(idxTest)));
fprintf('Accuracy: %.2f%%\n', acc*100);

figure;
confusionchart(Y(idxTest), pred);
title(sprintf('KNN (k=%d) — accuracy %.1f%%', k, acc*100));


