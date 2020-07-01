-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema yb
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema yb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `yb` DEFAULT CHARACTER SET utf8 ;
USE `yb` ;

-- -----------------------------------------------------
-- Table `yb`.`account`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `yb`.`account` (
  `emailId` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL COMMENT '이메일 아이디',
  `emailPsw` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL COMMENT '비밀번호',
  `name` VARCHAR(25) CHARACTER SET 'utf8' NOT NULL COMMENT '이름',
  `nickName` VARCHAR(25) CHARACTER SET 'utf8' NULL COMMENT '별명',
  `gender` VARCHAR(2) NOT NULL COMMENT '성별',
  `belong` VARCHAR(25) NOT NULL COMMENT '소속',
  `rank` VARCHAR(25) NOT NULL COMMENT '직위',
  `etc` VARCHAR(500) NULL COMMENT '비고',
  `status` VARCHAR(2) NOT NULL COMMENT '상태\n01. 활성\n02. 휴면\n03. 탈퇴',
  `regDate` DATE NOT NULL COMMENT '등록일시',
  `modyDate` DATE NULL COMMENT '수정일시',
  `dormancyDate` DATE NULL COMMENT '휴면일시',
  `secessionDate` DATE NULL COMMENT '탈퇴일시',
  `latelyDate` DATE NOT NULL COMMENT '최근접속일',
  `regIP` VARCHAR(45) NOT NULL COMMENT '등록 시 접속 IP',
  `modyIP` VARCHAR(45) NULL COMMENT '수정 시 접속 IP',
  PRIMARY KEY (`emailId`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `yb`.`human`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `yb`.`human` (
  `hContNum` INT NOT NULL COMMENT '휴먼등록 관리번호',
  `regEmailId` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL COMMENT '이메일 아이디',
  `regContPwd` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL COMMENT '휴먼관리 비밀번호',
  `coNameKor` VARCHAR(100) CHARACTER SET 'utf8' NOT NULL COMMENT '회사 이름 - 한글',
  `coNameEng` VARCHAR(50) NOT NULL COMMENT '회사 이름 - 영문',
  `foundedDate` DATE NOT NULL COMMENT '설립일',
  `coDiv` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '회사 구분\n01. 스타트업\n02. 중소기업',
  `corpDiv` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '법인구분\n01. 주식회사\n02. 유한회사\n03. 개인사업자\n04. 미설립',
  `coStatus` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '회사상태\n01. 비상장\n02. 상장\n03. 운영',
  `coAddr` VARCHAR(200) CHARACTER SET 'utf8' NOT NULL COMMENT '본사위치 - 법인기준 전체주소',
  `coEmail` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL COMMENT '회사 이메일',
  `coWeb` VARCHAR(255) CHARACTER SET 'utf8' NULL COMMENT '회사 웹사이트',
  `coLogo` VARCHAR(500) CHARACTER SET 'utf8' NULL COMMENT '회사 로고 - 링크',
  `representativeNameKor` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL COMMENT '대표자명 - 한글',
  `representativeNameEng` VARCHAR(25) CHARACTER SET 'utf8' NOT NULL COMMENT '대표자명 - 영문',
  `representativeNationality` VARCHAR(25) CHARACTER SET 'utf8' NOT NULL COMMENT '대표자 국적',
  `representativeGender` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '대표자 성별',
  `representativeFounderSame` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '대표자 / 설립자 동일 유무',
  `coRepresentative` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '공동대표자 유무',
  `coRepresentativeNameKor` VARCHAR(50) CHARACTER SET 'utf8' NULL COMMENT '공동대표자명 - 한글',
  `coRepresentativeNameEng` VARCHAR(25) CHARACTER SET 'utf8' NULL COMMENT '공동대표자명 - 영문',
  `serviceNameKor` VARCHAR(400) CHARACTER SET 'utf8' NOT NULL COMMENT '서비스명 - 한글',
  `serviceNameEng` VARCHAR(200) CHARACTER SET 'utf8' NOT NULL COMMENT '서비스명 - 영문',
  `serviceSummary` VARCHAR(400) CHARACTER SET 'utf8' NOT NULL COMMENT '서비스 설명 - 한 줄 요약',
  `tech` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '기술\n01. 클라우드\n02. 빅데이터 / 분석\n03. 인공지능\n04. 검색\n05. 전자상거래\n06. 결제\n07. 블록체인\n08. 크라우드펀딩\n09. 음악 / 영상 스트리밍\n10. VR / AR\n11. 3D그래픽 / 애니메이션\n12. 소셜네트워크\n13. 리얼타임 커뮤니케이션\n14. 로봇\n15. 드론\n16. 사물인터넷 / 센서\n17. 제조\n18. 연구개발\n19. 프로그램개발\n20. 게임개발\n21. 광고네트워크\n22. 광학\n23. 3D프린터\n24. 홀로그램\n25. 해당없음',
  `largeField` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '대분야\n01. 홈\n02. 생활\n03. 전자제품\n04. 음식\n05. 쇼핑\n06. 물류 / 유통\n07. 유아\n08. 애완동물\n09. 스포츠\n10. 패션\n11. 뷰티\n12. 게임\n13. 여행\n14. 교육\n15. 모임 / 행사\n16. 사회 / 봉사\n17. 바이오 / 의료\n18. 헬스케어\n19. 기업\n20. 광고마케팅\n21. 금융\n22. 보안\n23. 블록체인\n24. 엔터테인먼트\n25. 콘텐츠\n26. VR / AR\n27. 3D 프린터\n28. 항공기 / 드론\n29. 환경 / 에너지\n30. 자전거\n31. 오토바이\n32. 자동차\n33. 선박\n34. 건설\n35. 부동산\n36. 축산업\n37. 농산업\n38. 수산업\n39. 방송 / 언론\n40. 화학\n41. 군수\n42. 우주 / 항공\n',
  `smallField` VARCHAR(25) CHARACTER SET 'utf8' NOT NULL COMMENT '소분야 - 직접입력',
  `O2O` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT 'O2O\n01. O2O\n02. Online\n03. Offline\n',
  `buisnessType` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '사업형태\n01. 지원\n02. 제조 / 공급\n03. 유통\n04. 중개\n05. 대여\n06. 구독 / 멤버십\n07. 가맹\n08. 예약\n09. 연구 / 분석\n10. 육성\n11. 투자\n12. 인수합병\n13. 해당없음\n',
  `serviceType` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '서비스형태\n01. 웹사이트\n02. 모바일앱 - iOs\n03. 모바일앱 - AOS\n04. Dapp\n05. 하드웨어\n06. 소프르웨어\n07. API / SDK\n08. 상품\n09. 원료\n10. 공간\n11. 콘텐츠\n12. 채널\n13. 교육 / 컨설팅\n14. 물류서비스\n15. 건축 / 시공\n16. 부품\n17. 기계\n18. 공정 / 설비\n19. 펀드\n20. 지주회사\n',
  `serviceURL` VARCHAR(500) CHARACTER SET 'utf8' NULL COMMENT '서비스 url\n01. 웹사이트\n02. 소개자료링크\n',
  `similarService` VARCHAR(400) CHARACTER SET 'utf8' NULL COMMENT '유사 서비스 - 직접 입력',
  `serviceLogo` VARCHAR(500) CHARACTER SET 'utf8' NULL COMMENT '서비스로고 - 링크',
  `invStage` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '현재 투자 단계\n01. seed\n02. pre-A\n03. series-A\n04. series-B',
  `PreYearSaleVolume` VARCHAR(2) CHARACTER SET 'utf8' NULL COMMENT '전년도 매출 규모\n01. 없음\n02. 1억 이하\n03. 1~5억\n04. 5~10억\n05. 10억 이상',
  `invAttrTargetAmount` INT NOT NULL COMMENT '현재 투자 유치 목표금액(억)',
  `invFundPurpose` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '투자금 사용 목적\n01. 제품개발\n02. 시설투자\n03. 운전자금\n04. 마케팅\n05. 해외진출',
  `respresentativeTel` VARCHAR(15) CHARACTER SET 'utf8' NOT NULL COMMENT '대표자, 임원 연락처\n',
  `problemsToSolve` VARCHAR(500) CHARACTER SET 'utf8' NOT NULL COMMENT '풀어내고자 하는 문제 - 직접입력',
  `ourSolution` VARCHAR(500) CHARACTER SET 'utf8' NOT NULL COMMENT '우리팀의 해결책 - 솔루션',
  `aboutTeam` VARCHAR(500) CHARACTER SET 'utf8' NOT NULL COMMENT '팀 - 경력 / 자원 / 채널 위주의 서술',
  `invInfo` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '기존 투자정보 유무\n01. 네\n02. 없음',
  `invInfoAddintention` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '기존 투자정보 추가\n01. 네\n02. 아니요',
  `preInvDate` VARCHAR(2) CHARACTER SET 'utf8' NULL COMMENT '투자 날짜',
  `preInvStage` VARCHAR(2) CHARACTER SET 'utf8' NULL COMMENT '투자 단계\n01. seed\n02. pre-A\n03. series-A',
  `totalInvAmount` INT NULL COMMENT '총 투자금액 (억)',
  `preInvestor` VARCHAR(400) CHARACTER SET 'utf8' NULL COMMENT '투자자 - 직접 입력',
  `capital` INT NOT NULL COMMENT '자본금',
  `totalAssets` INT NOT NULL COMMENT '총 자산합계',
  `totalLiabilities` INT NOT NULL COMMENT '총부채',
  `numberOfEmp` INT NOT NULL COMMENT '종업원수',
  `coTel` VARCHAR(15) NOT NULL COMMENT '회사 TEL',
  PRIMARY KEY (`hContNum`, `regEmailId`),
  INDEX `fk_human_account1_idx` (`regEmailId` ASC))
ENGINE = MyISAM;


-- -----------------------------------------------------
-- Table `yb`.`angel`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `yb`.`angel` (
  `AContNum` INT NOT NULL COMMENT '엔젤등록 관리번호',
  `regEmailId` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL COMMENT '등록자 이메일 아이디',
  `regTel` INT NOT NULL COMMENT '등록자 연락처',
  `regContPwd` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL COMMENT '엔젤관리 비밀번호',
  `coNameKor` VARCHAR(100) CHARACTER SET 'utf8' NOT NULL COMMENT '회사 이름 - 한글',
  `coNameEng` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL COMMENT '회사 이름 - 영문',
  `representativeNameKor` VARCHAR(50) CHARACTER SET 'utf8' NOT NULL COMMENT '대표자명 - 한글',
  `representativeNameEng` VARCHAR(25) CHARACTER SET 'utf8' NOT NULL COMMENT '대표자명 - 영문',
  `coTel` INT NOT NULL COMMENT '회사 TEL',
  `invType` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '투자 유형\n01. 전략적투자자\n02. 재무적투자자',
  `corpDiv` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '법인구분\n01. 주식회사\n02. 유한회사\n03. 개인사업자\n04. 미설립',
  `coStatus` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '회사상태\n01. 비상장\n02. 상장\n03. 운영',
  `sectors` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '업종\nA. 농업, 임업 및 어업\nB. 광업\nC. 제조업\nD. 전기, 가스, 증기 및 수도사업\nE. 하수․폐기물 처리, 원료재생 및 환경복원업\nF. 건설업\nG. 도매 및 소매업\nH. 운수업\nI. 숙박 및 음식점업\nJ. 출판, 영상, 방송통신 및 정보서비스업\nK. 금융 및 보험업\nL. 부동산업 및 임대업\nM. 전문, 과학 및 기술 서비스업\nN. 사업시설관리 및 사업지원 서비스업\nO. 공공행정, 국방 및 사회보장 행정\nP. 교육 서비스업\nQ. 보건 및 사회복지 서비스업\nR. 예술, 스포츠 및 여가관련 서비스업\nS. 협회 및 단체, 수리 및 기타 개인 서비스업\nT. 가구내 고용활동 및 달리 분류되지 않은 자가 소비 생산활동\nU. 국제 및 외국기관\n',
  `item` VARCHAR(400) CHARACTER SET 'utf8' NOT NULL COMMENT '아이템 - 직접입력',
  `capital` INT NOT NULL COMMENT '보유현금',
  `coAddr` VARCHAR(200) CHARACTER SET 'utf8' NOT NULL COMMENT '본사위치 - 법인기준 전체주소',
  `hopCotype` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '희망 기업형태\n01. 주식회사\n02. 유한회사\n03. 개인사업자\n04. 미설립',
  `hopCoSect` VARCHAR(2) CHARACTER SET 'utf8' NOT NULL COMMENT '희망업종\nA. 농업, 임업 및 어업\nB. 광업\nC. 제조업\nD. 전기, 가스, 증기 및 수도사업\nE. 하수․폐기물 처리, 원료재생 및 환경복원업\nF. 건설업\nG. 도매 및 소매업\nH. 운수업\nI. 숙박 및 음식점업\nJ. 출판, 영상, 방송통신 및 정보서비스업\nK. 금융 및 보험업\nL. 부동산업 및 임대업\nM. 전문, 과학 및 기술 서비스업\nN. 사업시설관리 및 사업지원 서비스업\nO. 공공행정, 국방 및 사회보장 행정\nP. 교육 서비스업\nQ. 보건 및 사회복지 서비스업\nR. 예술, 스포츠 및 여가관련 서비스업\nS. 협회 및 단체, 수리 및 기타 개인 서비스업\nT. 가구내 고용활동 및 달리 분류되지 않은 자가 소비 생산활동\nU. 국제 및 외국기관\n',
  `hopCoItem` VARCHAR(400) CHARACTER SET 'utf8' NOT NULL COMMENT '희망아이템',
  `hopCoAddr` VARCHAR(200) CHARACTER SET 'utf8' NOT NULL COMMENT '희망소재지',
  `hopInvAmount` INT NOT NULL COMMENT '희망투자액',
  `hopSalesVolume` INT NOT NULL COMMENT '희망매출액',
  `hopOpProfit` INT NOT NULL COMMENT '희망영업이익',
  `etc` VARCHAR(400) CHARACTER SET 'utf8' NULL COMMENT '비고',
  PRIMARY KEY (`AContNum`, `regEmailId`),
  INDEX `fk_angel_account1_idx` (`regEmailId` ASC),
  CONSTRAINT `fk_angel_account1`
    FOREIGN KEY (`regEmailId`)
    REFERENCES `yb`.`account` (`emailId`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
