-- DROP SCHEMA public;

CREATE SCHEMA public AUTHORIZATION pg_database_owner;

COMMENT ON SCHEMA public IS 'standard public schema';

-- DROP SEQUENCE public.abilities_ability_no_seq;

CREATE SEQUENCE public.abilities_ability_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.abilities_ability_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.abilities_ability_no_seq TO neondb_owner;

-- DROP SEQUENCE public.char_group_relations_rel_no_seq;

CREATE SEQUENCE public.char_group_relations_rel_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.char_group_relations_rel_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.char_group_relations_rel_no_seq TO neondb_owner;

-- DROP SEQUENCE public.char_item_maps_own_no_seq;

CREATE SEQUENCE public.char_item_maps_own_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.char_item_maps_own_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.char_item_maps_own_no_seq TO neondb_owner;

-- DROP SEQUENCE public.char_relations_rel_no_seq;

CREATE SEQUENCE public.char_relations_rel_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.char_relations_rel_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.char_relations_rel_no_seq TO neondb_owner;

-- DROP SEQUENCE public.characters_char_no_seq;

CREATE SEQUENCE public.characters_char_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.characters_char_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.characters_char_no_seq TO neondb_owner;

-- DROP SEQUENCE public.core_rules_core_no_seq;

CREATE SEQUENCE public.core_rules_core_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.core_rules_core_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.core_rules_core_no_seq TO neondb_owner;

-- DROP SEQUENCE public.creature_skill_maps_map_no_seq;

CREATE SEQUENCE public.creature_skill_maps_map_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.creature_skill_maps_map_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.creature_skill_maps_map_no_seq TO neondb_owner;

-- DROP SEQUENCE public.creature_trait_maps_map_no_seq;

CREATE SEQUENCE public.creature_trait_maps_map_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.creature_trait_maps_map_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.creature_trait_maps_map_no_seq TO neondb_owner;

-- DROP SEQUENCE public.creatures_creature_no_seq;

CREATE SEQUENCE public.creatures_creature_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.creatures_creature_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.creatures_creature_no_seq TO neondb_owner;

-- DROP SEQUENCE public.event_entries_entry_no_seq;

CREATE SEQUENCE public.event_entries_entry_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.event_entries_entry_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.event_entries_entry_no_seq TO neondb_owner;

-- DROP SEQUENCE public.events_event_no_seq;

CREATE SEQUENCE public.events_event_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.events_event_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.events_event_no_seq TO neondb_owner;

-- DROP SEQUENCE public.group_relations_rel_no_seq;

CREATE SEQUENCE public.group_relations_rel_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.group_relations_rel_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.group_relations_rel_no_seq TO neondb_owner;

-- DROP SEQUENCE public.item_skill_maps_map_no_seq;

CREATE SEQUENCE public.item_skill_maps_map_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.item_skill_maps_map_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.item_skill_maps_map_no_seq TO neondb_owner;

-- DROP SEQUENCE public.item_trait_maps_map_no_seq;

CREATE SEQUENCE public.item_trait_maps_map_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.item_trait_maps_map_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.item_trait_maps_map_no_seq TO neondb_owner;

-- DROP SEQUENCE public.items_item_no_seq;

CREATE SEQUENCE public.items_item_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.items_item_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.items_item_no_seq TO neondb_owner;

-- DROP SEQUENCE public.lore_char_maps_map_no_seq;

CREATE SEQUENCE public.lore_char_maps_map_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.lore_char_maps_map_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.lore_char_maps_map_no_seq TO neondb_owner;

-- DROP SEQUENCE public.lore_item_maps_map_no_seq;

CREATE SEQUENCE public.lore_item_maps_map_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.lore_item_maps_map_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.lore_item_maps_map_no_seq TO neondb_owner;

-- DROP SEQUENCE public.lores_lore_no_seq;

CREATE SEQUENCE public.lores_lore_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.lores_lore_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.lores_lore_no_seq TO neondb_owner;

-- DROP SEQUENCE public.nations_ntn_no_seq;

CREATE SEQUENCE public.nations_ntn_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.nations_ntn_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.nations_ntn_no_seq TO neondb_owner;

-- DROP SEQUENCE public.ntn_trait_maps_map_no_seq;

CREATE SEQUENCE public.ntn_trait_maps_map_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.ntn_trait_maps_map_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.ntn_trait_maps_map_no_seq TO neondb_owner;

-- DROP SEQUENCE public.org_trait_maps_map_no_seq;

CREATE SEQUENCE public.org_trait_maps_map_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.org_trait_maps_map_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.org_trait_maps_map_no_seq TO neondb_owner;

-- DROP SEQUENCE public.organizations_org_no_seq;

CREATE SEQUENCE public.organizations_org_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.organizations_org_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.organizations_org_no_seq TO neondb_owner;

-- DROP SEQUENCE public.project_abilities_ability_no_seq;

CREATE SEQUENCE public.project_abilities_ability_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.project_abilities_ability_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.project_abilities_ability_no_seq TO neondb_owner;

-- DROP SEQUENCE public.project_skills_skill_no_seq;

CREATE SEQUENCE public.project_skills_skill_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.project_skills_skill_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.project_skills_skill_no_seq TO neondb_owner;

-- DROP SEQUENCE public.project_traits_trait_no_seq;

CREATE SEQUENCE public.project_traits_trait_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.project_traits_trait_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.project_traits_trait_no_seq TO neondb_owner;

-- DROP SEQUENCE public.projects_prj_no_seq;

CREATE SEQUENCE public.projects_prj_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.projects_prj_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.projects_prj_no_seq TO neondb_owner;

-- DROP SEQUENCE public.region_trait_maps_map_no_seq;

CREATE SEQUENCE public.region_trait_maps_map_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.region_trait_maps_map_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.region_trait_maps_map_no_seq TO neondb_owner;

-- DROP SEQUENCE public.regions_region_no_seq;

CREATE SEQUENCE public.regions_region_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.regions_region_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.regions_region_no_seq TO neondb_owner;

-- DROP SEQUENCE public.skills_skill_no_seq;

CREATE SEQUENCE public.skills_skill_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.skills_skill_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.skills_skill_no_seq TO neondb_owner;

-- DROP SEQUENCE public.traits_trait_no_seq;

CREATE SEQUENCE public.traits_trait_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 2147483647 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.traits_trait_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.traits_trait_no_seq TO neondb_owner;

-- DROP SEQUENCE public.users_user_no_seq;

CREATE SEQUENCE public.users_user_no_seq INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE;

-- Permissions

ALTER SEQUENCE public.users_user_no_seq OWNER TO neondb_owner;

GRANT ALL ON SEQUENCE public.users_user_no_seq TO neondb_owner;
-- public.abilities definition

-- Drop table

-- DROP TABLE public.abilities;

CREATE TABLE public.abilities (
    ability_no int8 GENERATED BY DEFAULT AS IDENTITY (
        INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE
    ) NOT NULL, -- 어빌리티 번호
    crt_dt timestamp(6) NULL, -- 생성 일시
    crt_no int8 NULL, -- 생성자 번호
    del_dt timestamp(6) NULL, -- 삭제 일시
    del_no int8 NULL, -- 삭제자 번호
    del_yn varchar(1) DEFAULT 'N'::character varying NULL, -- 삭제 여부
    shrn_yn varchar(1) DEFAULT 'N'::character varying NULL, -- 공유 여부
    updt_dt timestamp(6) NULL, -- 수정 일시
    updt_no int8 NULL, -- 수정자 번호
    use_yn varchar(1) DEFAULT 'Y'::character varying NULL, -- 사용 여부
    ability_nm varchar(255) NOT NULL, -- 어빌리티 명
    ability_domain varchar(255) NOT NULL, -- 권역 (Domain)
    ability_source varchar(255) NOT NULL, -- 원천 (Source)
    ability_lineage varchar(255) NOT NULL, -- 계통 (Lineage)
    ability_form varchar(255) NOT NULL, -- 형태 (Form)
    ability_tags text NULL, -- 태그 (Tags)
    ability_expln text NULL, -- 어빌리티 설명
    cast_time int4 NULL, -- 시전 시간
    cool_time int4 NULL, -- 쿨타임
    dmg_type varchar(255) NULL, -- 피해 유형
    stat_eff_type varchar(255) NULL, -- 상태 이상 유형
    trgt_type varchar(255) NULL, -- 대상 유형
    use_cnd text NULL, -- 사용 조건
    use_cost varchar(255) NULL, -- 사용 비용
    CONSTRAINT abilities_pkey PRIMARY KEY (ability_no)
);

CREATE INDEX idx_abilities_ability_nm ON public.abilities USING btree (ability_nm);

-- Permissions

ALTER TABLE public.abilities OWNER TO neondb_owner;

GRANT ALL ON TABLE public.abilities TO neondb_owner;

-- public.users definition

-- Drop table

-- DROP TABLE public.users;

CREATE TABLE public.users (
    user_no bigserial NOT NULL, -- 사용자 번호
    user_eml varchar(255) NULL, -- 사용자 이메일
    user_nm varchar(255) NULL, -- 사용자 명
    user_role varchar(255) NULL, -- 사용자 역할
    profl_img_url varchar(255) NULL, -- 프로필 이미지 URL
    biogp varchar(255) NULL, -- 자기소개
    enpswd varchar(255) NULL, -- 암호화 비밀번호
    resh_token varchar(255) NULL, -- 리프레시 토큰
    acnt_lck_yn varchar(1) NULL, -- 계정 잠금 여부
    lgn_fail_nmtm int4 NULL, -- 로그인 실패 횟수
    last_lgn_dt timestamp NULL, -- 마지막 로그인 일시
    last_lgn_ip varchar(255) NULL, -- 마지막 로그인 IP
    last_pswd_chg_dt timestamp NULL, -- 마지막 비밀번호 변경 일시
    eml_auth_yn varchar(1) NULL, -- 이메일 인증 여부
    mkt_recp_agre_yn varchar(1) NULL, -- 마케팅 수신 동의 여부
    use_yn varchar(1) NULL, -- 사용 여부
    shrn_yn varchar(1) NULL, -- 공유 여부
    del_yn varchar(1) NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT users_pkey PRIMARY KEY (user_no),
    CONSTRAINT users_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT users_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT users_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX idx_users_user_eml ON public.users USING btree (user_eml);

CREATE INDEX ix_users_user_eml ON public.users USING btree (user_eml);

-- Permissions

ALTER TABLE public.users OWNER TO neondb_owner;

GRANT ALL ON TABLE public.users TO neondb_owner;

-- public.projects definition

-- Drop table

-- DROP TABLE public.projects;

CREATE TABLE public.projects (
    prj_no bigserial NOT NULL, -- 프로젝트 번호
    user_no int8 NULL, -- 사용자 번호
    prj_nm varchar(255) NOT NULL, -- 프로젝트 명
    genre_type varchar(255) NULL, -- 장르 유형
    prj_desc text NULL, -- 프로젝트 설명 (요약)
    cvr_img_url varchar(255) NULL, -- 커버 이미지 URL
    prj_expln varchar NULL, -- 프로젝트 상세 설명
    prj_ver varchar(255) NULL, -- 프로젝트 버전
    use_yn varchar(1) DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar(1) DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar(1) DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT projects_pkey PRIMARY KEY (prj_no),
    CONSTRAINT projects_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT projects_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT projects_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no),
    CONSTRAINT projects_user_no_fkey FOREIGN KEY (user_no) REFERENCES public.users (user_no)
);

CREATE INDEX idx_projects_prj_nm ON public.projects USING btree (prj_nm);

CREATE INDEX idx_projects_user_no ON public.projects USING btree (user_no);

CREATE INDEX ix_projects_prj_nm ON public.projects USING btree (prj_nm);

CREATE INDEX ix_projects_user_no ON public.projects USING btree (user_no);

-- Permissions

ALTER TABLE public.projects OWNER TO neondb_owner;

GRANT ALL ON TABLE public.projects TO neondb_owner;

-- public.skills definition

-- Drop table

-- DROP TABLE public.skills;

CREATE TABLE public.skills (
    skill_no serial4 NOT NULL, -- 스킬 번호
    skill_nm varchar NOT NULL, -- 스킬 명
    skill_type varchar NOT NULL, -- 스킬 유형
    skill_lcls varchar NOT NULL, -- 스킬 대분류
    skill_expln text NULL, -- 스킬 설명
    trgt_type varchar NULL, -- 대상 유형
    dmg_type varchar NULL, -- 피해 유형
    stat_eff_type varchar NULL, -- 상태 이상 유형
    use_cost varchar NULL, -- 사용 비용
    cool_time varchar NULL, -- 쿨타임
    cast_time varchar NULL, -- 시전 시간
    use_cnd text NULL, -- 사용 조건
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT skills_pkey PRIMARY KEY (skill_no),
    CONSTRAINT skills_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT skills_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT skills_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_skills_skill_nm ON public.skills USING btree (skill_nm);

-- Permissions

ALTER TABLE public.skills OWNER TO neondb_owner;

GRANT ALL ON TABLE public.skills TO neondb_owner;

-- public.traits definition

-- Drop table

-- DROP TABLE public.traits;

CREATE TABLE public.traits (
    trait_no bigserial NOT NULL, -- 트레잇 번호
    trait_nm varchar(255) NOT NULL, -- 트레잇 명
    trait_expln text NULL, -- 트레잇 설명
    trait_lcls varchar(255) NOT NULL, -- 트레잇 대분류
    trait_mcls varchar(255) NOT NULL, -- 트레잇 중분류
    aply_trgt varchar(255) NULL, -- 적용 대상
    cnfl_trait_no int8 NULL, -- 상충 트레잇 번호
    use_yn varchar(1) DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar(1) DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar(1) DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT traits_pkey PRIMARY KEY (trait_no),
    CONSTRAINT traits_cnfl_trait_no_fkey FOREIGN KEY (cnfl_trait_no) REFERENCES public.traits (trait_no),
    CONSTRAINT traits_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT traits_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT traits_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX idx_traits_cnfl_trait_no ON public.traits USING btree (cnfl_trait_no);

CREATE INDEX idx_traits_trait_nm ON public.traits USING btree (trait_nm);

CREATE INDEX ix_traits_cnfl_trait_no ON public.traits USING btree (cnfl_trait_no);

CREATE INDEX ix_traits_trait_nm ON public.traits USING btree (trait_nm);

-- Permissions

ALTER TABLE public.traits OWNER TO neondb_owner;

GRANT ALL ON TABLE public.traits TO neondb_owner;

-- public.core_rules definition

-- Drop table

-- DROP TABLE public.core_rules;

CREATE TABLE public.core_rules (
    core_no serial4 NOT NULL, -- 코어 설정 번호
    prj_no int4 NOT NULL, -- 프로젝트 번호
    core_nm varchar NOT NULL, -- 코어 설정 명
    def_desc text NULL, -- 본질적 정의
    aply_scope text NULL, -- 적용 범위
    strc_elem text NULL, -- 코어 설정 요소
    mech_desc text NULL, -- 작동 원리
    narr_aply text NULL, -- 서사적 적용
    keywords varchar NULL, -- 핵심 키워드
    link_docs text NULL, -- 연관 설정
    rmk text NULL, -- 비고
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT core_rules_pkey PRIMARY KEY (core_no),
    CONSTRAINT core_rules_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT core_rules_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT core_rules_prj_no_fkey FOREIGN KEY (prj_no) REFERENCES public.projects (prj_no),
    CONSTRAINT core_rules_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_core_rules_prj_no ON public.core_rules USING btree (prj_no);

-- Permissions

ALTER TABLE public.core_rules OWNER TO neondb_owner;

GRANT ALL ON TABLE public.core_rules TO neondb_owner;

-- public.creatures definition

-- Drop table

-- DROP TABLE public.creatures;

CREATE TABLE public.creatures (
    creature_no serial4 NOT NULL, -- 크리처 번호
    prj_no int4 NOT NULL, -- 프로젝트 번호
    creature_nm varchar NOT NULL, -- 크리처 명
    creature_type varchar NOT NULL, -- 크리처 유형
    danger_grd varchar NULL, -- 위험 등급
    ident_stat varchar NOT NULL, -- 식별 상태
    creature_expln text NULL, -- 크리처 설명
    bio_char text NULL, -- 생물학적 특징
    lifespan_growth text NULL, -- 수명 및 성장
    body_feat text NULL, -- 신체적 특징
    sense_diet text NULL, -- 감각 및 식성
    reprod_info text NULL, -- 번식 정보
    eco_habit text NULL, -- 생태 습성
    habitat_env text NULL, -- 서식 환경
    lang_name text NULL, -- 언어 및 명명
    life_style text NULL, -- 생활 양식
    faith_taboo text NULL, -- 신앙 및 금기
    soc_struct text NULL, -- 사회 구조
    psych_tend text NULL, -- 심리적 성향
    abil_weak text NULL, -- 능력 및 약점
    civ_tech_lvl text NULL, -- 문명 기술 수준
    spec_trait text NULL, -- 특수 특성
    weakness text NULL, -- 약점
    est_eco text NULL, -- 경제 추정
    rumor_lore text NULL, -- 소문 및 전승
    poten_thrt text NULL, -- 잠재적 위협
    intel_lvl varchar NULL, -- 지능 수준
    drop_rsrc text NULL, -- 드랍 리소스
    hostile_rel varchar NULL, -- 적대 관계
    hist_desc text NULL, -- 역사적 서술
    rmk text NULL, -- 비고
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT creatures_pkey PRIMARY KEY (creature_no),
    CONSTRAINT creatures_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT creatures_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT creatures_prj_no_fkey FOREIGN KEY (prj_no) REFERENCES public.projects (prj_no),
    CONSTRAINT creatures_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_creatures_creature_nm ON public.creatures USING btree (creature_nm);

CREATE INDEX ix_creatures_prj_no ON public.creatures USING btree (prj_no);

-- Permissions

ALTER TABLE public.creatures OWNER TO neondb_owner;

GRANT ALL ON TABLE public.creatures TO neondb_owner;

-- public.events definition

-- Drop table

-- DROP TABLE public.events;

CREATE TABLE public.events (
    event_no serial4 NOT NULL, -- 사건 번호
    prj_no int4 NOT NULL, -- 프로젝트 번호
    event_nm varchar NOT NULL, -- 사건 명
    occur_time varchar NULL, -- 발생 시간
    occur_loc varchar NULL, -- 발생 장소
    smry text NULL, -- 요약
    cause_pub text NULL, -- 표면적 원인
    cause_real text NULL, -- 실질적 원인
    side_a_char text NULL, -- 진영 A 인물
    side_a_org text NULL, -- 진영 A 단체
    side_a_ntn text NULL, -- 진영 A 국가
    side_b_char text NULL, -- 진영 B 인물
    side_b_org text NULL, -- 진영 B 단체
    side_b_ntn text NULL, -- 진영 B 국가
    side_c_char text NULL, -- 진영 C 인물
    side_c_org text NULL, -- 진영 C 단체
    side_c_ntn text NULL, -- 진영 C 국가
    flow_trgr text NULL, -- 전개 발단
    flow_crisis text NULL, -- 전개 위기
    flow_climax text NULL, -- 전개 절정
    flow_concl text NULL, -- 전개 결말
    dmg_rslt text NULL, -- 피해 결과
    soc_chng text NULL, -- 사회적 변화
    curr_conn text NULL, -- 현재와의 연관성
    rec_official text NULL, -- 공식 기록
    truth_hid text NULL, -- 숨겨진 진실
    rmk text NULL, -- 비고
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT events_pkey PRIMARY KEY (event_no),
    CONSTRAINT events_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT events_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT events_prj_no_fkey FOREIGN KEY (prj_no) REFERENCES public.projects (prj_no),
    CONSTRAINT events_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_events_event_nm ON public.events USING btree (event_nm);

CREATE INDEX ix_events_prj_no ON public.events USING btree (prj_no);

-- Permissions

ALTER TABLE public.events OWNER TO neondb_owner;

GRANT ALL ON TABLE public.events TO neondb_owner;

-- public.group_relations definition

-- Drop table

-- DROP TABLE public.group_relations;

CREATE TABLE public.group_relations (
    rel_no serial4 NOT NULL, -- 관계 번호
    prj_no int4 NOT NULL, -- 프로젝트 번호
    src_type varchar NOT NULL, -- 원본 유형
    src_no int4 NOT NULL, -- 원본 번호
    trgt_type varchar NOT NULL, -- 대상 유형
    trgt_no int4 NOT NULL, -- 대상 번호
    rel_type varchar NOT NULL, -- 관계 유형
    rel_desc text NULL, -- 관계 설명
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT group_relations_pkey PRIMARY KEY (rel_no),
    CONSTRAINT group_relations_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT group_relations_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT group_relations_prj_no_fkey FOREIGN KEY (prj_no) REFERENCES public.projects (prj_no),
    CONSTRAINT group_relations_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_group_relations_prj_no ON public.group_relations USING btree (prj_no);

CREATE INDEX ix_group_relations_src_no ON public.group_relations USING btree (src_no);

CREATE INDEX ix_group_relations_trgt_no ON public.group_relations USING btree (trgt_no);

-- Permissions

ALTER TABLE public.group_relations OWNER TO neondb_owner;

GRANT ALL ON TABLE public.group_relations TO neondb_owner;

-- public.items definition

-- Drop table

-- DROP TABLE public.items;

CREATE TABLE public.items (
    item_no serial4 NOT NULL, -- 아이템 번호
    prj_no int4 NOT NULL, -- 프로젝트 번호
    item_nm varchar NOT NULL, -- 아이템 명
    cls_main varchar NOT NULL, -- 대분류
    cls_sub varchar NULL, -- 소분류
    item_grd varchar NULL, -- 아이템 등급
    logline varchar NULL, -- 로그라인
    app_desc text NULL, -- 외형 묘사
    visual_feat text NULL, -- 시각적 특징
    attr_type varchar NULL, -- 속성 유형
    dmg_type varchar NULL, -- 피해 유형
    main_func text NULL, -- 주요 기능
    sub_eff text NULL, -- 보조 효과
    spec_abil text NULL, -- 특수 능력
    ego_type varchar NULL, -- 자아 유형
    ego_desc text NULL, -- 자아 설명
    use_cond text NULL, -- 사용 조건
    use_mthd text NULL, -- 사용 방법
    trns_cond text NULL, -- 거래 조건
    strg_mthd text NULL, -- 보관 방법
    use_lmt text NULL, -- 사용 제한
    use_cost text NULL, -- 사용 비용
    side_eff text NULL, -- 부작용
    durability_desc text NULL, -- 내구도 설명
    hist_past text NULL, -- 과거 이력
    curr_stat text NULL, -- 현재 상태
    rmk text NULL, -- 비고
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT items_pkey PRIMARY KEY (item_no),
    CONSTRAINT items_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT items_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT items_prj_no_fkey FOREIGN KEY (prj_no) REFERENCES public.projects (prj_no),
    CONSTRAINT items_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_items_item_nm ON public.items USING btree (item_nm);

CREATE INDEX ix_items_prj_no ON public.items USING btree (prj_no);

-- Permissions

ALTER TABLE public.items OWNER TO neondb_owner;

GRANT ALL ON TABLE public.items TO neondb_owner;

-- public.lores definition

-- Drop table

-- DROP TABLE public.lores;

CREATE TABLE public.lores (
    lore_no serial4 NOT NULL, -- 로어 번호
    prj_no int4 NOT NULL, -- 프로젝트 번호
    lore_nm varchar NOT NULL, -- 로어 명
    lore_type varchar NULL, -- 로어 유형
    main_subj varchar NULL, -- 주요 주제
    smry text NULL, -- 요약
    trans_mthd varchar NULL, -- 전승 방법
    pub_perc text NULL, -- 대중의 인식
    lore_plot text NULL, -- 로어 플롯
    real_fact text NULL, -- 실제 사실
    dist_rsn text NULL, -- 왜곡 이유
    diff_desc text NULL, -- 차이점 설명
    cltr_impact text NULL, -- 문화적 영향
    plot_conn text NULL, -- 플롯 연관성
    rmk text NULL, -- 비고
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT lores_pkey PRIMARY KEY (lore_no),
    CONSTRAINT lores_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT lores_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT lores_prj_no_fkey FOREIGN KEY (prj_no) REFERENCES public.projects (prj_no),
    CONSTRAINT lores_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_lores_lore_nm ON public.lores USING btree (lore_nm);

CREATE INDEX ix_lores_prj_no ON public.lores USING btree (prj_no);

-- Permissions

ALTER TABLE public.lores OWNER TO neondb_owner;

GRANT ALL ON TABLE public.lores TO neondb_owner;

-- public.nations definition

-- Drop table

-- DROP TABLE public.nations;

CREATE TABLE public.nations (
    ntn_no serial4 NOT NULL, -- 국가 번호
    prj_no int4 NOT NULL, -- 프로젝트 번호
    ntn_nm varchar NOT NULL, -- 국가 명
    ntn_type varchar NULL, -- 국가 유형
    logline varchar NULL, -- 로그라인
    capital_nm varchar NULL, -- 수도 명
    ruler_txt varchar NULL, -- 통치자 정보
    pol_sys varchar NULL, -- 정치 체제
    admin_law text NULL, -- 행정 및 법률
    state_rlgn varchar NULL, -- 국교
    rlgn_desc text NULL, -- 종교 설명
    nat_idlg text NULL, -- 국가 이념
    main_plcy text NULL, -- 주요 정책
    taboo_act text NULL, -- 금기 행위
    dipl_plcy text NULL, -- 외교 정책
    intr_cnfl text NULL, -- 내부 갈등
    hidden_fact text NULL, -- 숨겨진 사실
    econ_struct text NULL, -- 경제 구조
    soc_cltr text NULL, -- 사회 문화
    mil_pwr text NULL, -- 군사력
    hist_desc text NULL, -- 역사적 서술
    curr_issue text NULL, -- 현재 이슈
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT nations_pkey PRIMARY KEY (ntn_no),
    CONSTRAINT nations_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT nations_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT nations_prj_no_fkey FOREIGN KEY (prj_no) REFERENCES public.projects (prj_no),
    CONSTRAINT nations_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_nations_ntn_nm ON public.nations USING btree (ntn_nm);

CREATE INDEX ix_nations_prj_no ON public.nations USING btree (prj_no);

-- Permissions

ALTER TABLE public.nations OWNER TO neondb_owner;

GRANT ALL ON TABLE public.nations TO neondb_owner;

-- public.ntn_trait_maps definition

-- Drop table

-- DROP TABLE public.ntn_trait_maps;

CREATE TABLE public.ntn_trait_maps (
    map_no serial4 NOT NULL, -- 매핑 번호
    ntn_no int4 NOT NULL, -- 국가 번호
    trait_no int4 NOT NULL, -- 트레잇 번호
    trait_type varchar NOT NULL, -- 트레잇 유형
    trait_rmk text NULL, -- 트레잇 비고
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT ntn_trait_maps_pkey PRIMARY KEY (map_no),
    CONSTRAINT ntn_trait_maps_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT ntn_trait_maps_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT ntn_trait_maps_ntn_no_fkey FOREIGN KEY (ntn_no) REFERENCES public.nations (ntn_no),
    CONSTRAINT ntn_trait_maps_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_ntn_trait_maps_ntn_no ON public.ntn_trait_maps USING btree (ntn_no);

CREATE INDEX ix_ntn_trait_maps_trait_no ON public.ntn_trait_maps USING btree (trait_no);

-- Permissions

ALTER TABLE public.ntn_trait_maps OWNER TO neondb_owner;

GRANT ALL ON TABLE public.ntn_trait_maps TO neondb_owner;

-- public.organizations definition

-- Drop table

-- DROP TABLE public.organizations;

CREATE TABLE public.organizations (
    org_no serial4 NOT NULL, -- 단체 번호
    prj_no int4 NOT NULL, -- 프로젝트 번호
    org_nm varchar NOT NULL, -- 단체 명
    org_type varchar NULL, -- 단체 유형
    logline varchar NULL, -- 로그라인
    org_theme varchar NULL, -- 단체 테마
    purp_pub varchar NULL, -- 표면적 목적
    purp_hid varchar NULL, -- 숨겨진 목적
    fnd_bg text NULL, -- 설립 배경
    org_strc text NULL, -- 조직 구조
    org_scale varchar NULL, -- 조직 규모
    join_cond text NULL, -- 가입 조건
    exit_rule text NULL, -- 탈퇴 규칙
    main_act text NULL, -- 주요 활동
    act_area text NULL, -- 활동 지역
    act_mthd text NULL, -- 활동 방식
    fund_src text NULL, -- 자금원
    key_fig text NULL, -- 핵심 인물
    hist_desc text NULL, -- 역사적 서술
    curr_stat text NULL, -- 현재 상태
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT organizations_pkey PRIMARY KEY (org_no),
    CONSTRAINT organizations_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT organizations_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT organizations_prj_no_fkey FOREIGN KEY (prj_no) REFERENCES public.projects (prj_no),
    CONSTRAINT organizations_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_organizations_org_nm ON public.organizations USING btree (org_nm);

CREATE INDEX ix_organizations_prj_no ON public.organizations USING btree (prj_no);

-- Permissions

ALTER TABLE public.organizations OWNER TO neondb_owner;

GRANT ALL ON TABLE public.organizations TO neondb_owner;

-- public.project_abilities definition

-- Drop table

-- DROP TABLE public.project_abilities;

CREATE TABLE public.project_abilities (
    ability_no int8 GENERATED BY DEFAULT AS IDENTITY (
        INCREMENT BY 1 MINVALUE 1 MAXVALUE 9223372036854775807 START 1 CACHE 1 NO CYCLE
    ) NOT NULL, -- 어빌리티 번호
    crt_dt timestamp(6) NULL, -- 생성 일시
    crt_no int8 NULL, -- 생성자 번호
    del_dt timestamp(6) NULL, -- 삭제 일시
    del_no int8 NULL, -- 삭제자 번호
    del_yn varchar(1) DEFAULT 'N'::character varying NULL, -- 삭제 여부
    shrn_yn varchar(1) DEFAULT 'N'::character varying NULL, -- 공유 여부
    updt_dt timestamp(6) NULL, -- 수정 일시
    updt_no int8 NULL, -- 수정자 번호
    use_yn varchar(1) DEFAULT 'Y'::character varying NULL, -- 사용 여부
    ability_nm varchar(255) NOT NULL, -- 어빌리티 명
    ability_domain varchar(255) NOT NULL, -- 권역 (Domain)
    ability_source varchar(255) NOT NULL, -- 원천 (Source)
    ability_lineage varchar(255) NOT NULL, -- 계통 (Lineage)
    ability_form varchar(255) NOT NULL, -- 형태 (Form)
    ability_tags text NULL, -- 태그 (Tags)
    ability_expln text NULL, -- 어빌리티 설명
    cast_time int4 NULL, -- 시전 시간
    cool_time int4 NULL, -- 쿨타임
    dmg_type varchar(255) NULL, -- 피해 유형
    stat_eff_type varchar(255) NULL, -- 상태 이상 유형
    trgt_type varchar(255) NULL, -- 대상 유형
    use_cnd text NULL, -- 사용 조건
    use_cost varchar(255) NULL, -- 사용 비용
    prj_no int8 NOT NULL, -- 프로젝트 번호
    CONSTRAINT project_abilities_pkey PRIMARY KEY (ability_no),
    CONSTRAINT fkt1wubm6pt5ko9mj6hg874e5pk FOREIGN KEY (prj_no) REFERENCES public.projects (prj_no)
);

CREATE INDEX idx_project_abilities_ability_nm ON public.project_abilities USING btree (ability_nm);

CREATE INDEX idx_project_abilities_prj_no ON public.project_abilities USING btree (prj_no);

-- Permissions

ALTER TABLE public.project_abilities OWNER TO neondb_owner;

GRANT ALL ON TABLE public.project_abilities TO neondb_owner;

-- public.project_skills definition

-- Drop table

-- DROP TABLE public.project_skills;

CREATE TABLE public.project_skills (
    skill_no serial4 NOT NULL, -- 스킬 번호
    prj_no int4 NOT NULL, -- 프로젝트 번호
    skill_nm varchar NOT NULL, -- 스킬 명
    skill_type varchar NOT NULL, -- 스킬 유형
    skill_lcls varchar NOT NULL, -- 스킬 대분류
    skill_expln text NULL, -- 스킬 설명
    trgt_type varchar NULL, -- 대상 유형
    dmg_type varchar NULL, -- 피해 유형
    stat_eff_type varchar NULL, -- 상태 이상 유형
    use_cost varchar NULL, -- 사용 비용
    cool_time varchar NULL, -- 쿨타임
    cast_time varchar NULL, -- 시전 시간
    use_cnd text NULL, -- 사용 조건
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT project_skills_pkey PRIMARY KEY (skill_no),
    CONSTRAINT project_skills_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT project_skills_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT project_skills_prj_no_fkey FOREIGN KEY (prj_no) REFERENCES public.projects (prj_no),
    CONSTRAINT project_skills_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_project_skills_prj_no ON public.project_skills USING btree (prj_no);

CREATE INDEX ix_project_skills_skill_nm ON public.project_skills USING btree (skill_nm);

-- Permissions

ALTER TABLE public.project_skills OWNER TO neondb_owner;

GRANT ALL ON TABLE public.project_skills TO neondb_owner;

-- public.project_traits definition

-- Drop table

-- DROP TABLE public.project_traits;

CREATE TABLE public.project_traits (
    trait_no bigserial NOT NULL, -- 트레잇 번호
    prj_no int8 NOT NULL, -- 프로젝트 번호
    trait_nm varchar(255) NOT NULL, -- 트레잇 명
    trait_expln text NULL, -- 트레잇 설명
    trait_lcls varchar(255) NOT NULL, -- 트레잇 대분류
    trait_mcls varchar(255) NOT NULL, -- 트레잇 중분류
    aply_trgt varchar(255) NULL, -- 적용 대상
    cnfl_trait_no int8 NULL, -- 상충 트레잇 번호
    cnfl_trait_type varchar(255) NULL, -- 상충 트레잇 유형
    use_yn varchar(1) DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar(1) DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar(1) DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT project_traits_pkey PRIMARY KEY (trait_no),
    CONSTRAINT project_traits_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT project_traits_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT project_traits_prj_no_fkey FOREIGN KEY (prj_no) REFERENCES public.projects (prj_no),
    CONSTRAINT project_traits_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX idx_project_traits_cnfl_trait_no ON public.project_traits USING btree (cnfl_trait_no);

CREATE INDEX idx_project_traits_prj_no ON public.project_traits USING btree (prj_no);

CREATE INDEX idx_project_traits_trait_nm ON public.project_traits USING btree (trait_nm);

CREATE INDEX ix_project_traits_cnfl_trait_no ON public.project_traits USING btree (cnfl_trait_no);

CREATE INDEX ix_project_traits_prj_no ON public.project_traits USING btree (prj_no);

CREATE INDEX ix_project_traits_trait_nm ON public.project_traits USING btree (trait_nm);

-- Permissions

ALTER TABLE public.project_traits OWNER TO neondb_owner;

GRANT ALL ON TABLE public.project_traits TO neondb_owner;

-- public.regions definition

-- Drop table

-- DROP TABLE public.regions;

CREATE TABLE public.regions (
    region_no serial4 NOT NULL, -- 지역 번호
    prj_no int4 NOT NULL, -- 프로젝트 번호
    up_region_no int4 NULL, -- 상위 지역 번호
    region_nm varchar NOT NULL, -- 지역 명
    region_type varchar NULL, -- 지역 유형
    explor_stat varchar NULL, -- 탐험 상태
    region_expln text NULL, -- 지역 설명
    loc_desc text NULL, -- 위치 묘사
    climate_env varchar NULL, -- 기후 환경
    terrain_feat text NULL, -- 지형 특징
    env_spec text NULL, -- 환경 특이사항
    func_feat text NULL, -- 기능적 특징
    danger_lvl varchar NULL, -- 위험 수준
    danger_fctr text NULL, -- 위험 요소
    inhabit_info text NULL, -- 거주 정보
    unknown_entity text NULL, -- 미지 존재
    main_fclty text NULL, -- 주요 시설
    rsrc_list text NULL, -- 자원 목록
    ntn_no int4 NULL, -- 국가 번호
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT regions_pkey PRIMARY KEY (region_no),
    CONSTRAINT regions_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT regions_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT regions_ntn_no_fkey FOREIGN KEY (ntn_no) REFERENCES public.nations (ntn_no),
    CONSTRAINT regions_prj_no_fkey FOREIGN KEY (prj_no) REFERENCES public.projects (prj_no),
    CONSTRAINT regions_up_region_no_fkey FOREIGN KEY (up_region_no) REFERENCES public.regions (region_no),
    CONSTRAINT regions_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_regions_ntn_no ON public.regions USING btree (ntn_no);

CREATE INDEX ix_regions_prj_no ON public.regions USING btree (prj_no);

CREATE INDEX ix_regions_region_nm ON public.regions USING btree (region_nm);

CREATE INDEX ix_regions_up_region_no ON public.regions USING btree (up_region_no);

-- Permissions

ALTER TABLE public.regions OWNER TO neondb_owner;

GRANT ALL ON TABLE public.regions TO neondb_owner;

-- public."characters" definition

-- Drop table

-- DROP TABLE public."characters";

CREATE TABLE public."characters" (
    char_no serial4 NOT NULL, -- 캐릭터 번호
    prj_no int4 NOT NULL, -- 프로젝트 번호
    char_nm varchar NOT NULL, -- 캐릭터 명
    alias_nm varchar NULL, -- 이명/별칭
    role_type varchar NOT NULL, -- 역할 유형
    logline text NULL, -- 로그라인
    narr_func varchar NULL, -- 서사적 기능
    race_no int4 NULL, -- 종족 번호
    ntn_no int4 NULL, -- 국가 번호
    org_no int4 NULL, -- 소속 단체 번호
    org_rank varchar NULL, -- 단체 내 직위
    origin_desc text NULL, -- 출신 배경
    join_rsn text NULL, -- 가입 이유
    org_rel_stat varchar NULL, -- 단체 관계 상태
    real_age varchar NULL, -- 실제 나이
    app_age varchar NULL, -- 외관 나이
    gender varchar NULL, -- 성별
    sex_orient varchar NULL, -- 성적 지향
    sex_pref text NULL, -- 성적 취향
    height_val varchar NULL, -- 키
    weight_val varchar NULL, -- 몸무게
    body_desc text NULL, -- 신체 묘사
    health_stat text NULL, -- 건강 상태
    dsbl_desc text NULL, -- 장애/특이사항
    visual_pnt text NULL, -- 시각적 포인트
    fst_impr text NULL, -- 첫인상
    mslw_lv1_phys text NULL, -- 욕구 1단계(생리적)
    mslw_lv2_safe text NULL, -- 욕구 2단계(안전)
    mslw_lv3_soc text NULL, -- 욕구 3단계(사회적)
    mslw_lv4_estm text NULL, -- 욕구 4단계(존중)
    mslw_lv5_self text NULL, -- 욕구 5단계(자아실현)
    like_list text NULL, -- 호(Like)
    hate_list text NULL, -- 불호(Hate)
    align_ord varchar NULL, -- 성향(질서/혼돈)
    align_moral varchar NULL, -- 성향(선/악)
    core_val varchar NULL, -- 핵심 가치
    val_cnfl text NULL, -- 가치관 갈등
    world_view text NULL, -- 세계관
    pers_pos text NULL, -- 긍정적 성격
    pers_neg text NULL, -- 부정적 성격
    main_emot varchar NULL, -- 주된 감정
    tone_type varchar NULL, -- 어조/말투
    soc_mthd text NULL, -- 사회적 상호작용 방식
    habit_desc text NULL, -- 습관/버릇
    sign_line text NULL, -- 대표 대사
    emot_expr_json text NULL, -- 감정 표현 방식
    core_desire text NULL, -- 핵심 욕망
    core_dfcn text NULL, -- 핵심 결핍
    core_taboo text NULL, -- 핵심 금기
    goal_short text NULL, -- 단기 목표
    obstacle text NULL, -- 장애물
    exp_cost text NULL, -- 예상 대가
    rule_abandon text NULL, -- 버릴 규칙
    rule_keep text NULL, -- 지킬 규칙
    moral_accept text NULL, -- 도덕적 허용선
    moral_reject text NULL, -- 도덕적 거부선
    cnfl_trgr text NULL, -- 갈등 유발 요인
    emot_accum text NULL, -- 감정 축적
    expl_type varchar NULL, -- 설명 유형
    self_perc text NULL, -- 자아 인식
    ext_perc text NULL, -- 타인의 인식
    secret_json text NULL, -- 비밀
    trma_core varchar NULL, -- 핵심 트라우마
    trma_evnt text NULL, -- 트라우마 사건
    false_blf text NULL, -- 잘못된 믿음
    main_fear text NULL, -- 주요 두려움
    trma_trgr text NULL, -- 트라우마 트리거
    cmbt_styl text NULL, -- 전투 스타일
    cmbt_str text NULL, -- 전투 강점
    cmbt_weak text NULL, -- 전투 약점
    abil_cost text NULL, -- 능력 대가
    arc_start text NULL, -- 아크 시작점
    arc_end text NULL, -- 아크 종료점
    rmk text NULL, -- 비고
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT characters_pkey PRIMARY KEY (char_no),
    CONSTRAINT characters_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT characters_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT characters_ntn_no_fkey FOREIGN KEY (ntn_no) REFERENCES public.nations (ntn_no),
    CONSTRAINT characters_org_no_fkey FOREIGN KEY (org_no) REFERENCES public.organizations (org_no),
    CONSTRAINT characters_prj_no_fkey FOREIGN KEY (prj_no) REFERENCES public.projects (prj_no),
    CONSTRAINT characters_race_no_fkey FOREIGN KEY (race_no) REFERENCES public.creatures (creature_no),
    CONSTRAINT characters_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_characters_char_nm ON public.characters USING btree (char_nm);

CREATE INDEX ix_characters_ntn_no ON public.characters USING btree (ntn_no);

CREATE INDEX ix_characters_org_no ON public.characters USING btree (org_no);

CREATE INDEX ix_characters_prj_no ON public.characters USING btree (prj_no);

CREATE INDEX ix_characters_race_no ON public.characters USING btree (race_no);

-- Permissions

ALTER TABLE public."characters" OWNER TO neondb_owner;

GRANT ALL ON TABLE public."characters" TO neondb_owner;

-- public.creature_skill_maps definition

-- Drop table

-- DROP TABLE public.creature_skill_maps;

CREATE TABLE public.creature_skill_maps (
    map_no serial4 NOT NULL, -- 매핑 번호
    creature_no int4 NOT NULL, -- 크리처 번호
    skill_no int4 NOT NULL, -- 스킬 번호
    skill_type varchar NOT NULL, -- 스킬 유형
    prof_lvl varchar NULL, -- 숙련도
    skill_rmk text NULL, -- 스킬 비고
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT creature_skill_maps_pkey PRIMARY KEY (map_no),
    CONSTRAINT creature_skill_maps_creature_no_fkey FOREIGN KEY (creature_no) REFERENCES public.creatures (creature_no),
    CONSTRAINT creature_skill_maps_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT creature_skill_maps_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT creature_skill_maps_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_creature_skill_maps_creature_no ON public.creature_skill_maps USING btree (creature_no);

CREATE INDEX ix_creature_skill_maps_skill_no ON public.creature_skill_maps USING btree (skill_no);

-- Permissions

ALTER TABLE public.creature_skill_maps OWNER TO neondb_owner;

GRANT ALL ON TABLE public.creature_skill_maps TO neondb_owner;

-- public.creature_trait_maps definition

-- Drop table

-- DROP TABLE public.creature_trait_maps;

CREATE TABLE public.creature_trait_maps (
    map_no serial4 NOT NULL, -- 매핑 번호
    creature_no int4 NOT NULL, -- 크리처 번호
    trait_no int4 NOT NULL, -- 트레잇 번호
    trait_type varchar NOT NULL, -- 트레잇 유형
    trait_rmk text NULL, -- 트레잇 비고
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT creature_trait_maps_pkey PRIMARY KEY (map_no),
    CONSTRAINT creature_trait_maps_creature_no_fkey FOREIGN KEY (creature_no) REFERENCES public.creatures (creature_no),
    CONSTRAINT creature_trait_maps_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT creature_trait_maps_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT creature_trait_maps_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_creature_trait_maps_creature_no ON public.creature_trait_maps USING btree (creature_no);

CREATE INDEX ix_creature_trait_maps_trait_no ON public.creature_trait_maps USING btree (trait_no);

-- Permissions

ALTER TABLE public.creature_trait_maps OWNER TO neondb_owner;

GRANT ALL ON TABLE public.creature_trait_maps TO neondb_owner;

-- public.event_entries definition

-- Drop table

-- DROP TABLE public.event_entries;

CREATE TABLE public.event_entries (
    entry_no serial4 NOT NULL, -- 참가 번호
    event_no int4 NOT NULL, -- 사건 번호
    entry_type varchar NOT NULL, -- 참가 유형
    entry_trgt_no int4 NOT NULL, -- 참가 대상 번호
    entry_side varchar NULL, -- 참가 진영
    role_desc text NULL, -- 역할 설명
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT event_entries_pkey PRIMARY KEY (entry_no),
    CONSTRAINT event_entries_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT event_entries_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT event_entries_event_no_fkey FOREIGN KEY (event_no) REFERENCES public.events (event_no),
    CONSTRAINT event_entries_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_event_entries_entry_trgt_no ON public.event_entries USING btree (entry_trgt_no);

CREATE INDEX ix_event_entries_event_no ON public.event_entries USING btree (event_no);

-- Permissions

ALTER TABLE public.event_entries OWNER TO neondb_owner;

GRANT ALL ON TABLE public.event_entries TO neondb_owner;

-- public.item_skill_maps definition

-- Drop table

-- DROP TABLE public.item_skill_maps;

CREATE TABLE public.item_skill_maps (
    map_no serial4 NOT NULL, -- 매핑 번호
    item_no int4 NOT NULL, -- 아이템 번호
    skill_no int4 NOT NULL, -- 스킬 번호
    skill_type varchar NOT NULL, -- 스킬 유형
    prof_lvl varchar NULL, -- 숙련도
    skill_rmk text NULL, -- 스킬 비고
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT item_skill_maps_pkey PRIMARY KEY (map_no),
    CONSTRAINT item_skill_maps_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT item_skill_maps_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT item_skill_maps_item_no_fkey FOREIGN KEY (item_no) REFERENCES public.items (item_no),
    CONSTRAINT item_skill_maps_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_item_skill_maps_item_no ON public.item_skill_maps USING btree (item_no);

CREATE INDEX ix_item_skill_maps_skill_no ON public.item_skill_maps USING btree (skill_no);

-- Permissions

ALTER TABLE public.item_skill_maps OWNER TO neondb_owner;

GRANT ALL ON TABLE public.item_skill_maps TO neondb_owner;

-- public.item_trait_maps definition

-- Drop table

-- DROP TABLE public.item_trait_maps;

CREATE TABLE public.item_trait_maps (
    map_no serial4 NOT NULL, -- 매핑 번호
    item_no int4 NOT NULL, -- 아이템 번호
    trait_no int4 NOT NULL, -- 트레잇 번호
    trait_type varchar NOT NULL, -- 트레잇 유형
    trait_rmk text NULL, -- 트레잇 비고
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT item_trait_maps_pkey PRIMARY KEY (map_no),
    CONSTRAINT item_trait_maps_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT item_trait_maps_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT item_trait_maps_item_no_fkey FOREIGN KEY (item_no) REFERENCES public.items (item_no),
    CONSTRAINT item_trait_maps_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_item_trait_maps_item_no ON public.item_trait_maps USING btree (item_no);

CREATE INDEX ix_item_trait_maps_trait_no ON public.item_trait_maps USING btree (trait_no);

-- Permissions

ALTER TABLE public.item_trait_maps OWNER TO neondb_owner;

GRANT ALL ON TABLE public.item_trait_maps TO neondb_owner;

-- public.lore_char_maps definition

-- Drop table

-- DROP TABLE public.lore_char_maps;

CREATE TABLE public.lore_char_maps (
    map_no serial4 NOT NULL, -- 매핑 번호
    lore_no int4 NOT NULL, -- 로어 번호
    char_no int4 NOT NULL, -- 캐릭터 번호
    role_desc text NULL, -- 역할 설명
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT lore_char_maps_pkey PRIMARY KEY (map_no),
    CONSTRAINT lore_char_maps_char_no_fkey FOREIGN KEY (char_no) REFERENCES public."characters" (char_no),
    CONSTRAINT lore_char_maps_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT lore_char_maps_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT lore_char_maps_lore_no_fkey FOREIGN KEY (lore_no) REFERENCES public.lores (lore_no),
    CONSTRAINT lore_char_maps_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_lore_char_maps_char_no ON public.lore_char_maps USING btree (char_no);

CREATE INDEX ix_lore_char_maps_lore_no ON public.lore_char_maps USING btree (lore_no);

-- Permissions

ALTER TABLE public.lore_char_maps OWNER TO neondb_owner;

GRANT ALL ON TABLE public.lore_char_maps TO neondb_owner;

-- public.lore_item_maps definition

-- Drop table

-- DROP TABLE public.lore_item_maps;

CREATE TABLE public.lore_item_maps (
    map_no serial4 NOT NULL, -- 매핑 번호
    lore_no int4 NOT NULL, -- 로어 번호
    item_no int4 NOT NULL, -- 아이템 번호
    role_desc text NULL, -- 역할 설명
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT lore_item_maps_pkey PRIMARY KEY (map_no),
    CONSTRAINT lore_item_maps_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT lore_item_maps_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT lore_item_maps_item_no_fkey FOREIGN KEY (item_no) REFERENCES public.items (item_no),
    CONSTRAINT lore_item_maps_lore_no_fkey FOREIGN KEY (lore_no) REFERENCES public.lores (lore_no),
    CONSTRAINT lore_item_maps_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_lore_item_maps_item_no ON public.lore_item_maps USING btree (item_no);

CREATE INDEX ix_lore_item_maps_lore_no ON public.lore_item_maps USING btree (lore_no);

-- Permissions

ALTER TABLE public.lore_item_maps OWNER TO neondb_owner;

GRANT ALL ON TABLE public.lore_item_maps TO neondb_owner;

-- public.org_trait_maps definition

-- Drop table

-- DROP TABLE public.org_trait_maps;

CREATE TABLE public.org_trait_maps (
    map_no serial4 NOT NULL, -- 매핑 번호
    org_no int4 NOT NULL, -- 단체 번호
    trait_no int4 NOT NULL, -- 트레잇 번호
    trait_type varchar NOT NULL, -- 트레잇 유형
    trait_rmk text NULL, -- 트레잇 비고
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT org_trait_maps_pkey PRIMARY KEY (map_no),
    CONSTRAINT org_trait_maps_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT org_trait_maps_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT org_trait_maps_org_no_fkey FOREIGN KEY (org_no) REFERENCES public.organizations (org_no),
    CONSTRAINT org_trait_maps_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_org_trait_maps_org_no ON public.org_trait_maps USING btree (org_no);

CREATE INDEX ix_org_trait_maps_trait_no ON public.org_trait_maps USING btree (trait_no);

-- Permissions

ALTER TABLE public.org_trait_maps OWNER TO neondb_owner;

GRANT ALL ON TABLE public.org_trait_maps TO neondb_owner;

-- public.region_trait_maps definition

-- Drop table

-- DROP TABLE public.region_trait_maps;

CREATE TABLE public.region_trait_maps (
    map_no serial4 NOT NULL, -- 매핑 번호
    region_no int4 NOT NULL, -- 지역 번호
    trait_no int4 NOT NULL, -- 트레잇 번호
    trait_type varchar NOT NULL, -- 트레잇 유형
    trait_rmk text NULL, -- 트레잇 비고
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT region_trait_maps_pkey PRIMARY KEY (map_no),
    CONSTRAINT region_trait_maps_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT region_trait_maps_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT region_trait_maps_region_no_fkey FOREIGN KEY (region_no) REFERENCES public.regions (region_no),
    CONSTRAINT region_trait_maps_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_region_trait_maps_region_no ON public.region_trait_maps USING btree (region_no);

CREATE INDEX ix_region_trait_maps_trait_no ON public.region_trait_maps USING btree (trait_no);

-- Permissions

ALTER TABLE public.region_trait_maps OWNER TO neondb_owner;

GRANT ALL ON TABLE public.region_trait_maps TO neondb_owner;

-- public.char_group_relations definition

-- Drop table

-- DROP TABLE public.char_group_relations;

CREATE TABLE public.char_group_relations (
    rel_no serial4 NOT NULL, -- 관계 번호
    char_no int4 NOT NULL, -- 캐릭터 번호
    trgt_type varchar NOT NULL, -- 대상 유형
    trgt_no int4 NOT NULL, -- 대상 번호
    rel_type varchar NOT NULL, -- 관계 유형
    rel_desc text NULL, -- 관계 설명
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT char_group_relations_pkey PRIMARY KEY (rel_no),
    CONSTRAINT char_group_relations_char_no_fkey FOREIGN KEY (char_no) REFERENCES public."characters" (char_no),
    CONSTRAINT char_group_relations_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT char_group_relations_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT char_group_relations_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_char_group_relations_char_no ON public.char_group_relations USING btree (char_no);

CREATE INDEX ix_char_group_relations_trgt_ref_no ON public.char_group_relations USING btree (trgt_no);

-- Permissions

ALTER TABLE public.char_group_relations OWNER TO neondb_owner;

GRANT ALL ON TABLE public.char_group_relations TO neondb_owner;

-- public.char_item_maps definition

-- Drop table

-- DROP TABLE public.char_item_maps;

CREATE TABLE public.char_item_maps (
    map_no serial4 NOT NULL, -- 매핑 번호
    char_no int4 NOT NULL, -- 캐릭터 번호
    item_no int4 NOT NULL, -- 아이템 번호
    possw_type varchar NOT NULL, -- 소유 유형
    acq_route text NULL, -- 획득 경로
    use_desc text NULL, -- 사용 설명
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT char_item_maps_pkey PRIMARY KEY (map_no),
    CONSTRAINT char_item_maps_char_no_fkey FOREIGN KEY (char_no) REFERENCES public."characters" (char_no),
    CONSTRAINT char_item_maps_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT char_item_maps_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT char_item_maps_item_no_fkey FOREIGN KEY (item_no) REFERENCES public.items (item_no),
    CONSTRAINT char_item_maps_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_char_item_maps_char_no ON public.char_item_maps USING btree (char_no);

CREATE INDEX ix_char_item_maps_item_no ON public.char_item_maps USING btree (item_no);

-- Permissions

ALTER TABLE public.char_item_maps OWNER TO neondb_owner;

GRANT ALL ON TABLE public.char_item_maps TO neondb_owner;

-- public.char_relations definition

-- Drop table

-- DROP TABLE public.char_relations;

CREATE TABLE public.char_relations (
    rel_no serial4 NOT NULL, -- 관계 번호
    src_char_no int4 NOT NULL, -- 원본 캐릭터 번호
    trgt_char_no int4 NOT NULL, -- 대상 캐릭터 번호
    rel_type varchar NULL, -- 관계 유형
    trust_lvl int4 NULL, -- 신뢰도
    rel_desc text NULL, -- 관계 설명
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT char_relations_pkey PRIMARY KEY (rel_no),
    CONSTRAINT char_relations_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT char_relations_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT char_relations_src_char_no_fkey FOREIGN KEY (src_char_no) REFERENCES public."characters" (char_no),
    CONSTRAINT char_relations_trgt_char_no_fkey FOREIGN KEY (trgt_char_no) REFERENCES public."characters" (char_no),
    CONSTRAINT char_relations_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_char_relations_src_char_no ON public.char_relations USING btree (src_char_no);

CREATE INDEX ix_char_relations_trgt_char_no ON public.char_relations USING btree (trgt_char_no);

-- Permissions

ALTER TABLE public.char_relations OWNER TO neondb_owner;

GRANT ALL ON TABLE public.char_relations TO neondb_owner;

-- public.char_skill_maps definition

-- Drop table

-- DROP TABLE public.char_skill_maps;

CREATE TABLE public.char_skill_maps (
    map_no serial4 NOT NULL, -- 매핑 번호
    char_no int4 NOT NULL, -- 캐릭터 번호
    skill_no int4 NOT NULL, -- 스킬 번호
    skill_type varchar NOT NULL, -- 스킬 유형
    prof_lvl varchar NULL, -- 숙련도
    skill_rmk text NULL, -- 스킬 비고
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT char_skill_maps_pkey PRIMARY KEY (map_no),
    CONSTRAINT char_skill_maps_char_no_fkey FOREIGN KEY (char_no) REFERENCES public."characters" (char_no),
    CONSTRAINT char_skill_maps_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT char_skill_maps_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT char_skill_maps_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_char_skill_maps_char_no ON public.char_skill_maps USING btree (char_no);

CREATE INDEX ix_char_skill_maps_skill_no ON public.char_skill_maps USING btree (skill_no);

-- Permissions

ALTER TABLE public.char_skill_maps OWNER TO neondb_owner;

GRANT ALL ON TABLE public.char_skill_maps TO neondb_owner;

-- public.char_trait_maps definition

-- Drop table

-- DROP TABLE public.char_trait_maps;

CREATE TABLE public.char_trait_maps (
    map_no serial4 NOT NULL, -- 매핑 번호
    char_no int4 NOT NULL, -- 캐릭터 번호
    trait_no int4 NOT NULL, -- 트레잇 번호
    trait_type varchar NOT NULL, -- 트레잇 유형
    trait_rmk text NULL, -- 트레잇 비고
    use_yn varchar DEFAULT 'Y'::character varying NULL, -- 사용 여부
    shrn_yn varchar DEFAULT 'Y'::character varying NULL, -- 공유 여부
    del_yn varchar DEFAULT 'N'::character varying NULL, -- 삭제 여부
    crt_no int8 NULL, -- 생성자 번호
    crt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 생성 일시
    updt_no int8 NULL, -- 수정자 번호
    updt_dt timestamp DEFAULT CURRENT_TIMESTAMP NULL, -- 수정 일시
    del_no int8 NULL, -- 삭제자 번호
    del_dt timestamp NULL, -- 삭제 일시
    CONSTRAINT char_trait_maps_pkey PRIMARY KEY (map_no),
    CONSTRAINT char_trait_maps_char_no_fkey FOREIGN KEY (char_no) REFERENCES public."characters" (char_no),
    CONSTRAINT char_trait_maps_crt_no_fkey FOREIGN KEY (crt_no) REFERENCES public.users (user_no),
    CONSTRAINT char_trait_maps_del_no_fkey FOREIGN KEY (del_no) REFERENCES public.users (user_no),
    CONSTRAINT char_trait_maps_updt_no_fkey FOREIGN KEY (updt_no) REFERENCES public.users (user_no)
);

CREATE INDEX ix_char_trait_maps_char_no ON public.char_trait_maps USING btree (char_no);

CREATE INDEX ix_char_trait_maps_trait_no ON public.char_trait_maps USING btree (trait_no);

-- Permissions

ALTER TABLE public.char_trait_maps OWNER TO neondb_owner;

GRANT ALL ON TABLE public.char_trait_maps TO neondb_owner;

-- Permissions

GRANT ALL ON SCHEMA public TO pg_database_owner;

GRANT USAGE ON SCHEMA public TO public;

ALTER DEFAULT PRIVILEGES FOR ROLE cloud_admin IN SCHEMA public GRANT SELECT, REFERENCES, MAINTAIN, INSERT, DELETE, TRUNCATE, UPDATE, TRIGGER ON TABLES TO neon_superuser WITH GRANT OPTION;

ALTER DEFAULT PRIVILEGES FOR ROLE cloud_admin IN SCHEMA public
GRANT
SELECT, USAGE,
UPDATE ON SEQUENCES TO neon_superuser
WITH
GRANT OPTION;